import os
import datetime
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

def get_audio_input():
    with sr.Microphone() as source:
        speak("Say something!")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand what you said. Could you please repeat that?")
        return get_audio_input()

def display_menu():
    speak("What would you like to do?")
    speak("first. View today's diary entry")
    speak("second. Add a new diary entry")
    speak("third. Exit the program")

def read_entry(date):
    try:
        with open(f"{date}.txt", "r") as file:
            speak(file.read())
    except FileNotFoundError:
        speak(f"No diary entry found for {date}. Would you like to add a new entry for today?")

def add_entry(date):
    speak("What would you like to add to your diary for today?")
    entry = get_audio_input()
    with open(f"{date}.txt", "a") as file:
        file.write(entry + "\n")
    speak("Diary entry added successfully.")

if __name__ == "__main__":
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    while True:
        display_menu()
        choice = get_audio_input()
        if choice == "first":
            read_entry(date)
        elif choice == "second":
            add_entry(date)
        elif choice == "third":
            speak("Goodbye!")
            break
        else:
            speak("Invalid choice. Please try again.")
