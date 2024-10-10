# TTS with Emotion Analysis

This project demonstrates how to combine **Text-to-Speech (TTS)** with **emotion analysis** to create a more natural and expressive speech synthesis. The script uses **Hugging Face's `transformers` library** for emotion analysis and **`pyttsx3` library** for TTS.

## Features

- Analyze the emotion of input text using a sentiment analysis pipeline.
- Adjust TTS settings (rate, volume) based on the detected emotion:
  - **Positive emotion**: Faster speed, higher volume.
  - **Negative emotion**: Slower speed, lower volume.
  - **Neutral emotion**: Moderate speed and volume.

## Prerequisites

- Python 3.x
- The following Python libraries:
  - `pyttsx3`
  - `transformers`
  - `torch` (required by `transformers`)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```
2. **Set up a virtual environment (optional but recommended):**
   ```bash
   source .venv/bin/activate  # On macOS/Linux
   # .venv\Scripts\activate  # On Windows
   ```
3. **Install the required libraries:**
   ```bash
   # python version <= 3.11
   pip install --upgrade setuptools wheel
   pip install setuptools
   pip install numpy==1.25.2
   pip install pyttsx3 transformers torch
   ```

## Usage

1. **Run the script:**
   ```bash
   python tts_with_emotion_analysis.py
   ```
2. **Modify the text to analyze**
   - Open <code>python tts_with_emotion_analysis.py</code> and modify the <code>text</code> variable to the text you want to analyze and synthesize.
   ```python
   text = "i feel so good"
   ```
3. **Listen to the output:**
   - The script will analyze the emotion of the input text and adjust the TTS settings accordingly, then play the synthesized speech.

## How It Works

1. The script first performs emotion analysis on the input text using Hugging Face's <code>transformers</code> library.
2. Based on the detected emotion (<code>POSITIVE</code>, <code>NEGATIVE</code>, or <code>NEUTRAL</code>), the TTS settings (rate, volume) are adjusted.
3. The <code>pyttsx3</code> library is used to convert the text to speech and play it.

## Example

**If the input text is <code>"i feel so good today"</code>, the script will:**

- Detect the emotion as <code>POSITIVE</code>
- Set the speech rate to be faster and the volume to be louder
- Convert the text to speech and play it with the adjusted settings

## Limitations

- The <code>pyttsx3</code> library does not support direct pitch adjustment, so only the rate(speed) and volume are adjusted based on the emotion.
- Emotion analysis results may not be perfectly accurate, as the depend on the underlying model's capabilities.

## License

This project is licensed under the MIT License. See the LICENSE file for more details

## Contributing

Feel free to submit issues or pull requests if you would like to contribute to the project or suggest improvements.

## Acknowledgements

- Hugging Face's transformers library for the emotion analysis model.
- pyttsx3 for the TTS functionality.
