import speech_recognition as sr
from googletrans import Translator
import pyttsx3

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

def speak_text(text, language='en'):
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

    print(f"You will be speaking in English and translations will be in {language2}.")
    speak_text(f"You will be speaking in English and translations will be in {language2}.")

    while True:
        command = recognize_speech(recognizer, microphone)
        if command:
            if command.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                speak_text("Exiting the program. Goodbye!")
                break
            
            print("Translating...")
            translated_text = translate_text(command, target_language='en')  # Translate to English first
            translated_text = translate_text(translated_text, target_language=language2)  # Then translate to target language
            print(f"Translated text ({language2}):", translated_text)
            speak_text(f"The translation in {language2} is: {translated_text}")
