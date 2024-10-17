import os
import pyttsx3
import speech_recognition as sr


# initialize text-to-speech engine
engine = pyttsx3.init()

# use speech recognition to get user response
r = sr.Recognizer()
with sr.Microphone() as source:
    print(f"What would you like to do Master? You can say 'listen to music', 'write in my diary', 'talk to Sakha', or 'exit'.")
    engine.say(f"What would you like to do? You can say 'listen to music', 'write in my diary', 'talk to Sakha', or 'exit'.")
    engine.runAndWait()
    print("Listening*********")
    audio = r.listen(source)


try:
    user_response = r.recognize_google(audio)
    print(f"You said: {user_response}")
    if user_response.lower() == "listen to music":
        os.system('song1.py')
    elif user_response.lower() == "write in my diary":
        os.system('dairy.py')
    elif user_response.lower() == "talk to Sakha":
        os.system('chatgptbot.py')
    elif user_response.lower() == "exit":
        print("Goodbye!")
    else:
        print("Sorry, I didn't understand your response.")

except sr.UnknownValueError:
    print("Sorry, I didn't understand your response.")
