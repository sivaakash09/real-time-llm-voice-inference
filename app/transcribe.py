import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()


def transcribe_audio(input_audio_path: str, output_text_path: str) -> None:
    audio_path = Path(input_audio_path)
    transcript_path = Path(output_text_path)

    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    transcript_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Transcribing: {audio_path}")

    with audio_path.open("rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=audio_file,
        )

    transcript_path.write_text(transcript.text, encoding="utf-8")

    print(f"Transcript saved to: {transcript_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:")
        print("python3 -m app.transcribe <input_audio_path> <output_text_path>")
        sys.exit(1)

    transcribe_audio(sys.argv[1], sys.argv[2])