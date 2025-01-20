# Audio to Text Transcription

This repository contains a script for converting audio files to text using OpenAI's Whisper model. The script takes an audio file as input and outputs the transcribed text.

## Features

- Converts audio files to text using OpenAI's Whisper model.
- Command-line interface for easy usage.
- Outputs the transcribed text to a file named `output.txt`.

## Requirements

- Python 3.x
- OpenAI Python client library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Install the required Python packages:

   ```bash
   pip install openai argparse
   ```

## Usage

To use the script, run the following command:

```bash
python stt.py --audio_file_path example.wav
```

This will convert the audio file `example.wav` to text and save the output in `output.txt`.

## API Key

Set your OpenAI API key in the `settings.py` file.
