import speech_recognition as sr
from googletrans import Translator, constants
import pyttsx3
from gtts import gTTS
from playsound import playsound
import tempfile
import os

def recognize_speech(recognizer, microphone):
    with microphone as source:
        print("Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, couldn't understand audio.")
        return None
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))
        return None

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def resolve_language_code(name, default="en"):
    """Return a language code given a language name or code."""
    name = name.lower()
    if name in constants.LANGCODES:
        return constants.LANGCODES[name]
    for code, lang in constants.LANGUAGES.items():
        if lang.lower() == name or code.lower() == name:
            return code
    return default

def speak_text(text, language='en', use_gtts=True):
    """Speak the given text.

    If ``use_gtts`` is True, use gTTS for more natural-sounding speech.
    Falls back to ``pyttsx3`` when gTTS fails or when ``use_gtts`` is False.
    """
    if use_gtts:
        temp_path = None
        try:
            tts = gTTS(text=text, lang=language)
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
                temp_path = fp.name
                tts.save(temp_path)
            playsound(temp_path)
            return
        except Exception as exc:
            print(f"gTTS failed ({exc}); falling back to pyttsx3")
        finally:
            if temp_path and os.path.exists(temp_path):
                os.remove(temp_path)

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Welcome to the Voice Translator!")
    speak_text("Welcome to the Voice Translator!")
    print("This program listens for voice commands and translates them into the specified language.")
    speak_text("This program listens for voice commands and translates them into the specified language.")
    print("To exit the program, say 'exit'.")
    speak_text("To exit the program, say 'exit'.")

    # Ask the user to choose languages for speaking and translation
    language1 = 'en'  # Source language is always English
    language2 = input("Please choose the translation language (e.g., 'Nepali' or 'Hindi'): ").strip().lower()
    language2_code = resolve_language_code(language2)

    print(f"You will be speaking in English and translations will be in {language2}.")
    speak_text(f"You will be speaking in English and translations will be in {language2}.", language=language2_code)

    while True:
        command = recognize_speech(recognizer, microphone)
        if command:
            if command.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                speak_text("Exiting the program. Goodbye!")
                break
            
            print("Translating...")
            translated_text = translate_text(command, target_language='en')  # Translate to English first
            translated_text = translate_text(translated_text, target_language=language2_code)  # Then translate to target language
            print(f"Translated text ({language2}):", translated_text)
            speak_text(f"The translation in {language2} is: {translated_text}", language=language2_code)
