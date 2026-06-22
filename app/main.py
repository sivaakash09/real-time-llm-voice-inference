import os
import json
import asyncio
import websockets

from twilio.rest import Client
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import Response

from app.scenarios import get_scenario, build_patient_prompt


load_dotenv()

TEST_NUMBER = "+18054398008"

app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Pretty Good AI voice tester server",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.api_route("/twiml", methods=["GET", "POST"])
def twiml(scenario_id: str = "appointment_basic"):
    """
    Twilio requests this endpoint when the call starts.
    It tells Twilio to connect call audio to our WebSocket.
    """

    public_domain = os.getenv("PUBLIC_DOMAIN")

    if not public_domain:
        return Response("Missing PUBLIC_DOMAIN", status_code=500)

    # Validate scenario early so a bad scenario ID fails clearly.
    try:
        get_scenario(scenario_id)
    except ValueError as e:
        return Response(str(e), status_code=400)

    xml = f"""
<Response>
    <Connect>
        <Stream url="wss://{public_domain}/media-stream/{scenario_id}" />
    </Connect>
</Response>
""".strip()

    return Response(content=xml, media_type="text/xml")


@app.websocket("/media-stream/{scenario_id}")
async def media_stream(websocket: WebSocket, scenario_id: str):
    """
    Live bridge:
    Twilio phone audio -> OpenAI Realtime
    OpenAI patient voice -> Twilio phone call
    """

    await websocket.accept()
    print("Twilio media stream connected.")
    print(f"Using scenario ID: {scenario_id}")

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Missing OPENAI_API_KEY")
        await websocket.close()
        return

    try:
        scenario = get_scenario(scenario_id)
    except ValueError as e:
        print(e)
        await websocket.close()
        return

    patient_prompt = build_patient_prompt(scenario)

    openai_url = "wss://api.openai.com/v1/realtime?model=gpt-realtime-2"

    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    stream_sid = None

    try:
        async with websockets.connect(
            openai_url,
            additional_headers=headers,
        ) as openai_ws:
            print("Connected to OpenAI from media stream.")

            session_update = {
                "type": "session.update",
                "session": {
                    "type": "realtime",
                    "model": "gpt-realtime-2",
                    "instructions": patient_prompt,
                    "output_modalities": ["audio"],
                    "audio": {
                        "input": {
                            "format": {
                                "type": "audio/pcmu"
                            },
                            "turn_detection": {
                                "type": "semantic_vad"
                            },
                        },
                        "output": {
                            "format": {
                                "type": "audio/pcmu"
                            },
                            "voice": "marin",
                        },
                    },
                },
            }

            await openai_ws.send(json.dumps(session_update))
            print("OpenAI session configured.")

            async def twilio_to_openai():
                nonlocal stream_sid

                try:
                    while True:
                        message = await websocket.receive_text()
                        data = json.loads(message)

                        event_type = data.get("event")

                        if event_type == "start":
                            stream_sid = data["start"]["streamSid"]
                            print(f"Twilio stream started: {stream_sid}")

                        elif event_type == "media":
                            audio_payload = data["media"]["payload"]

                            await openai_ws.send(json.dumps({
                                "type": "input_audio_buffer.append",
                                "audio": audio_payload,
                            }))

                        elif event_type == "stop":
                            print("Twilio stream stopped.")
                            break

                except WebSocketDisconnect:
                    print("Twilio websocket disconnected.")
                except Exception as e:
                    print("Twilio to OpenAI error:", e)

            async def openai_to_twilio():
                try:
                    async for openai_message in openai_ws:
                        response = json.loads(openai_message)
                        event_type = response.get("type")

                        if event_type in ["session.created", "session.updated"]:
                            print(f"OpenAI event: {event_type}")

                        elif event_type in [
                            "response.audio.delta",
                            "response.output_audio.delta",
                        ]:
                            if stream_sid is None:
                                continue

                            audio_delta = response.get("delta")

                            if not audio_delta:
                                continue

                            await websocket.send_text(json.dumps({
                                "event": "media",
                                "streamSid": stream_sid,
                                "media": {
                                    "payload": audio_delta
                                },
                            }))

                        elif event_type in [
                            "response.audio_transcript.delta",
                            "response.output_audio_transcript.delta",
                        ]:
                            print("BOT:", response.get("delta", ""), end="", flush=True)

                        elif event_type == "response.done":
                            print("\nOpenAI response done.")

                        elif event_type == "error":
                            print("OpenAI error:", response)

                except Exception as e:
                    print("OpenAI to Twilio error:", e)

            task_twilio = asyncio.create_task(twilio_to_openai())
            task_openai = asyncio.create_task(openai_to_twilio())

            done, pending = await asyncio.wait(
                [task_twilio, task_openai],
                return_when=asyncio.FIRST_COMPLETED,
            )

            for task in pending:
                task.cancel()

    except Exception as e:
        print("Media stream error:")
        print(e)


def validate_test_number(number: str) -> None:
    if number != TEST_NUMBER:
        raise ValueError("Call only the test number")


def check_env() -> None:
    required_vars = [
        "TWILIO_ACCOUNT_SID",
        "TWILIO_AUTH_TOKEN",
        "TWILIO_PHONE_NUMBER",
        "OPENAI_API_KEY",
        "PUBLIC_DOMAIN",
    ]

    missing = []

    for var in required_vars:
        if not os.getenv(var):
            missing.append(var)

    if missing:
        print("env var missing")
        for var in missing:
            print(f"-{var}")
    else:
        print("All env var found")


async def test_openai_realtime_connection() -> None:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Missing OPENAI_API_KEY")
        return

    url = "wss://api.openai.com/v1/realtime?model=gpt-realtime-2"

    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    try:
        async with websockets.connect(
            url,
            additional_headers=headers,
        ) as openai_ws:
            print("Connected to OpenAI Realtime API.")
    except Exception as e:
        print("OpenAI Realtime connection failed:")
        print(e)


def start_test_call() -> None:
    validate_test_number(TEST_NUMBER)

    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
    public_domain = os.getenv("PUBLIC_DOMAIN")

    scenario_id = os.getenv("SCENARIO_ID", "appointment_basic")

    # Validate scenario before making a paid phone call.
    get_scenario(scenario_id)

    if not account_sid or not auth_token or not twilio_number or not public_domain:
        raise ValueError("Missing Twilio environment variables.")

    client = Client(account_sid, auth_token)

    twiml_url = f"https://{public_domain}/twiml?scenario_id={scenario_id}"

    print(f"Starting call to: {TEST_NUMBER}")
    print(f"Selected scenario ID: {scenario_id}")
    print(f"Using TwiML URL: {twiml_url}")

    call = client.calls.create(
        to=TEST_NUMBER,
        from_=twilio_number,
        url=twiml_url,
        record=True,
        recording_channels="dual",
    )

    print(f"Call started. SID: {call.sid}")


if __name__ == "__main__":
    validate_test_number(TEST_NUMBER)
    print(f"Safety check passed. Allowed number: {TEST_NUMBER}")

    scenario_id = os.getenv("SCENARIO_ID", "appointment_basic")
    scenario = get_scenario(scenario_id)

    print(f"Selected scenario ID: {scenario_id}")
    print("Loaded scenario:")
    print(f"- Name: {scenario['name']}")
    print(f"- Patient: {scenario['patient_name']}")
    print(f"- Goal: {scenario['goal']}")
    print(f"- Opening line: {scenario['opening_line']}")

    check_env()

    if os.getenv("START_CALL") == "true":
        start_test_call()
    else:
        print("START_CALL is not true, so no phone call was made.")