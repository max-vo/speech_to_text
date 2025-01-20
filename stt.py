import argparse
from openai import OpenAI

from settings import OPENAI_API_KEY

def convert_audio_to_text(audio_file_path):
    client = OpenAI(api_key=OPENAI_API_KEY)
    audio_file= open(audio_file_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    return transcription.text

if __name__ == "__main__":
    """
    Command-line interface for converting audio files to text using OpenAI's Whisper model.

    This script requires an audio file path as an argument and outputs the transcribed text.

    Usage:
        python stt.py --audio_file_path <path_to_audio_file>

    Arguments:
        --audio_file_path: The path to the audio file to be transcribed.
    """
    # get args
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio_file_path", type=str, required=True)
    args = parser.parse_args()
    audio_file_path = args.audio_file_path
    print(f"Converting audio file {audio_file_path} to text...")
    text = convert_audio_to_text(audio_file_path)
    print(text)
    with open("output.txt", "w") as f:
        f.write(text)
    print("Output written to output.txt")
