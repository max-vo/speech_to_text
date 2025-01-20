import argparse
import os
from openai import OpenAI

def convert_audio_to_text(audio_file_path):
    # get the API key from the settings.py file
    from settings import OPENAI_API_KEY
    if not OPENAI_API_KEY or OPENAI_API_KEY == "":
        # try to get the API key from the environment variable
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
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

    # check if the file exists
    if not os.path.exists(audio_file_path):
        print(f"File {audio_file_path} does not exist")
        exit(1)

    # check if the file is an audio file / supported format
    if not audio_file_path.endswith((".wav", ".mp3", ".m4a", ".ogg", ".flac")):
        print(f"File {audio_file_path} is not an audio file")
        exit(1)
    
    new_path = "".join(audio_file_path.split(".")[:-1]) + ".txt"
    
    print(f"Converting audio file {audio_file_path} to text...")
    text = convert_audio_to_text(audio_file_path)
    print(text)
    with open(new_path, "w") as f:
        f.write(text)
    print(f"Output written to {new_path}")
