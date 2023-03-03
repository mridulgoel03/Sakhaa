import os, sys
import pyttsx3
import speech_recognition as sr
import webbrowser
import openai

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()

openai.api_key = "Enter your key here"
model_engine = "text-davinci-002"

r = sr.Recognizer()

if __name__ == "__main__":
    speak("Hello, Sakhhaa here. How may I help you?")
    while True:
        with sr.Microphone() as source:
            speak("Listening your voice....")
            audio = r.listen(source)
            try:
                command = r.recognize_google(audio)
                speak("You said: " + command)
                response = openai.Completion.create(
                    engine=model_engine,
                    prompt='Answer the question: ' + command,
                    max_tokens=1024,
                    n=1,
                    stop=None,
                    temperature=0.5,
                ).choices[0].text
                speak(response)
                if "youtube" in command.lower():
                    speak("Opening youtube.com....")
                    print("Opening Youtube.com....")
                    webbrowser.open("https://www.youtube.com/")
                elif "wikipedia" in command.lower():
                    speak("Opening Wikipedia....")
                    print("Opening Wikipedia....")
                    webbrowser.open("https://wikipedia.org/")
                elif "close" in command.lower():
                    speak("Stopping Program....")
                    print("Stopping Program....")
                    sys.exit()
            except sr.UnknownValueError:
                speak("I couldn't understand your voice. Can you say that again?")
                print("Unrecognized Voice. Say that again please.")

