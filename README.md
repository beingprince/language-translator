# language-translator
Voice Translator: Python program using speech recognition &amp; translation libraries. Converts spoken commands to a specified language and reads the translation aloud.

## Features

- **Speech recognition** via `SpeechRecognition`.
- **Translation** powered by `googletrans`.
- **Natural voice output** using `gTTS` with a fallback to `pyttsx3` when offline.

## Usage

Install the dependencies and run `translator.py`:

```bash
pip install -r requirements.txt
python translator.py
```

Speak in English and the program will translate your speech into the language you choose. Say `exit` to quit.
