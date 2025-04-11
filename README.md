# Voice Cloning System

A voice cloning system that combines MeloTTS and OpenVoice to generate high-quality, natural-sounding voice from text using voice cloning technology.

## Overview

This project provides a simple interface to generate text-to-speech audio with the ability to clone a target voice from a reference audio sample. It combines two powerful technologies:

- [MeloTTS](https://github.com/myshell-ai/MeloTTS): High-quality multi-lingual text-to-speech library
- [OpenVoice](https://github.com/myshell-ai/OpenVoice): Versatile instant voice cloning technology

## Features

- **Voice Cloning**: Clone any voice from a reference audio sample
- **Multi-language Support**: Works with English, Spanish, French, Chinese, Japanese, and Korean
- **Adjustable Speech Parameters**: Control speech speed
- **Easy Playback**: Built-in audio playback functionality

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd VoiceClone
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Download additional resources:

```bash
python -m unidic download
```

## Usage


### Requirement
Python 3.9.x

### Basic Usage

Run the main script to generate speech with the default settings:

```bash
python main.py
```

This will:

1. Generate speech using MeloTTS
2. Clone the voice style from a reference speaker
3. Save the result to `outputs_v2/output.wav`
4. Play the generated audio

### Customizing the Voice

You can modify `voice_test.py` to:

- Change the reference speaker audio file
- Modify the text content
- Adjust speech speed
- Change the language

## How It Works

1. **Text-to-Speech Generation**: First, MeloTTS converts input text to speech.
2. **Voice Cloning**: Then, OpenVoice extracts the tone color embedding from a reference voice and applies it to the generated speech.
3. **Output**: The final audio is saved to the `outputs_v2` directory.

## Project Structure

- `main.py`: Entry point that creates a VoiceTest instance and calls the openvoice method
- `voice_test.py`: Contains the VoiceTest class with methods for TTS and voice cloning
- `modules/MeloTTS`: MeloTTS library for multi-lingual text-to-speech
- `modules/OpenVoice`: OpenVoice library for voice cloning
- `outputs_v2`: Directory for output audio files

## Advanced Usage

### Using Different Languages

The system supports multiple languages. To use a different language, modify the `language` parameter in the `melotts` method:

```python
model = TTS(
    language="ES",  # Change to ES, FR, ZH, JP, KR
    device="cpu",
    ckpt_path="modules/MeloTTS/checkpoints/checkpoint.pth",
    config_path="modules/MeloTTS/checkpoints/config.json",
)
```

### Using Different Reference Voices

To clone a different voice, change the `reference_speaker` path in the `openvoice` method:

```python
reference_speaker = "path/to/your/reference/audio.mp3"
```

## License

This project uses components with MIT licenses. See the respective license files in the `modules` directory for more details.

## Acknowledgements

- [MyShell.ai](https://myshell.ai) for creating MeloTTS and OpenVoice
- Authors: Wenliang Zhao, Xumin Yu, and Zengyi Qin
