# real-time-llm-voice-inference

A latency-sensitive conversational voice system built with FastAPI, Twilio Media Streams, WebSockets, and the OpenAI Realtime API. The system streams live call audio bidirectionally, manages conversation sessions, and evaluates reliability across healthcare-oriented interaction scenarios.

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

Create your environment file:

```bash
cp .env.example .env
```

Fill in `.env`:

```env
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
OPENAI_API_KEY=your_openai_api_key
PUBLIC_DOMAIN=your_ngrok_domain
```

Do not include `https://` in `PUBLIC_DOMAIN`.

Example:

```env
PUBLIC_DOMAIN=example.ngrok-free.app
```

Do not commit `.env`.

## Run Instructions

Start the FastAPI server:

```bash
uvicorn app.main:app --reload --port 6060
```

In another terminal, start ngrok:

```bash
ngrok http 6060
```

Copy the ngrok domain into `.env` as `PUBLIC_DOMAIN`.

Check server health:

```bash
curl http://localhost:6060/health
```

## Run a Call

Run one scenario with a single command:

```bash
SCENARIO_ID=appointment_basic START_CALL=true python3 -m app.main
```

Available scenarios:

```bash
SCENARIO_ID=appointment_basic START_CALL=true python3 -m app.main
SCENARIO_ID=reschedule_existing START_CALL=true python3 -m app.main
SCENARIO_ID=cancel_appointment START_CALL=true python3 -m app.main
SCENARIO_ID=medication_refill START_CALL=true python3 -m app.main
SCENARIO_ID=office_hours_location START_CALL=true python3 -m app.main
SCENARIO_ID=insurance_question START_CALL=true python3 -m app.main
SCENARIO_ID=weekend_edge_case START_CALL=true python3 -m app.main
SCENARIO_ID=unclear_request START_CALL=true python3 -m app.main
SCENARIO_ID=interruption_test START_CALL=true python3 -m app.main
SCENARIO_ID=date_confusion START_CALL=true python3 -m app.main
SCENARIO_ID=referral_question START_CALL=true python3 -m app.main
SCENARIO_ID=duplicate_appointment_question START_CALL=true python3 -m app.main
SCENARIO_ID=billing_question START_CALL=true python3 -m app.main
```

## Save and Transcribe a Recording

Each call is stored like this:

```text
calls/call_01/
├── notes.md
├── recording.mp3
└── transcript.txt
```

After downloading the Twilio recording:

```bash
mkdir -p calls/call_01
mv ~/Downloads/EXACT_DOWNLOADED_FILENAME.mp3 calls/call_01/recording.mp3
```

Transcribe it:

```bash
python3 -m app.transcribe calls/call_01/recording.mp3 calls/call_01/transcript.txt
```

View the transcript:

```bash
cat calls/call_01/transcript.txt
```

## Project Structure

```text
PRETTY_GOOD_AI/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── scenarios.py
│   └── transcribe.py
├── calls/
│   ├── call_01/
│   │   ├── notes.md
│   │   ├── recording.mp3
│   │   └── transcript.txt
│   ├── call_02/
│   │   ├── notes.md
│   │   ├── recording.mp3
│   │   └── transcript.txt
│   └── ...
├── ARCHITECTURE.md
├── BUG_REPORT.md
├── ITERATION_NOTES.md
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

## Deliverables

This repository includes:

- Working Python voice bot
- Clear setup and run instructions
- Architecture document
- 13 call attempts with recordings and transcripts
- Bug report
- Iteration notes showing AI-assisted debugging
- Loom walkthrough
- AI-debugging screen recording

## Loom Videos

- [Walkthrough of the overall approach](https://www.loom.com/share/a9c907b98fc647c18a040ce5c6bfbecb)
- [Prompting AI to debug and improve bot](https://www.loom.com/share/7516ad6dc11b4dd8a7e73275f697e5ff)

## Notes

The bot only calls the Pretty Good AI test number.

Secrets are stored in `.env` and excluded from GitHub.
