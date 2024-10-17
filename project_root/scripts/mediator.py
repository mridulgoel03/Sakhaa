import os
import pyttsx3
import speech_recognition as sr

class Mediator:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_for_command(self):
        with sr.Microphone() as source:
            self.speak("What would you like to do? You can say 'listen to music', 'write in my diary', 'talk to Sakha', or 'exit'.")
            audio = self.recognizer.listen(source)
        try:
            return self.recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't understand. Please try again.")
            return self.listen_for_command()

    def run(self):
        while True:
            user_response = self.listen_for_command()
            if user_response == "listen to music":
                os.system('scripts/song1.py')
            elif user_response == "write in my diary":
                os.system('scripts/dairy.py')
            elif user_response == "talk to sakha":
                os.system('scripts/chatgptbot.py')  # Placeholder for actual script
            elif user_response == "exit":
                print("Goodbye!")
                break
            else:
                print("Sorry, I didn't understand your response.")

if __name__ == "__main__":
    mediator = Mediator()
    mediator.run()
