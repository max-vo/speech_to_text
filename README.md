# Audio to Text Transcription

This repository contains a script for converting audio files to text using OpenAI's Whisper model. The script takes an audio file as input and outputs the transcribed text.

## Features

- Converts audio files to text using OpenAI's Whisper model.
- Command-line interface for easy usage.
- Outputs the transcribed text to a file named `output.txt`.

## Requirements

- Python 3.x

### Install Python

You can download Python from [here](https://www.python.org/downloads/).

IMPORTANT: When installing Python, make sure to check the option to add Python to your PATH.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key in the `settings.py` file. You can get your API key from [here](https://platform.openai.com/api-keys).

## Usage

To use the script, run the following command:

```bash
python stt.py --audio_file_path <path_to_audio_file>
```

This will convert the audio file to text and save the output in `output.txt`.

