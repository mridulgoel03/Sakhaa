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

openai.api_key = "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"
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
                elif "discord" in command.lower():
                    speak("Opening Discord....")
                    print("Opening Discord....")
                    os.startfile("C:/Users/Kunal/AppData/Local/Discord/Update.exe")
                elif "close" in command.lower():
                    speak("Stopping Program....")
                    print("Stopping Program....")
                    sys.exit()
            except sr.UnknownValueError:
                speak("I couldn't understand your voice. Can you say that again?")
                print("Unrecognized Voice. Say that again please.")


# import openai
# import speech_recognition as sr
# import pyttsx3

# openai.api_key = "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"

# def generate_response(prompt):
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#         languages=["en", "hi"],
#     )
#     return response.choices[0].text

# def listen_for_speech():
#     recognizer = sr.Recognizer()
#     microphone = sr.Microphone()
#     with microphone as source:
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
#     return recognizer.recognize_google(audio)

# def speak_text(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# while True:
#     print("Listening for speech...")
#     prompt = listen_for_speech()
#     response = generate_response(prompt)
#     print("Chatbot: " + response)
#     speak_text("Chatbot: " + response)

# import openai

# openai.api_key = "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"

# def generate_response(prompt):
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#     return response.choices[0].text

# while True:
#     prompt = input("You: ")
#     response = generate_response(prompt)
#     print("Chatbot: " + response)
