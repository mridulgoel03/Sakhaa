# Sakhaa
<h1>Sakhaa your Ai friend</h1>
This code is a chatbot program called "Sakha" that can listen to voice commands and perform tasks such as playing music, writing in a diary, talking to the user, and answering questions.

The program uses several Python libraries, including tkinter, subprocess, os, pyttsx3, speech_recognition, webbrowser, and pygame. It also uses the OpenAI API for generating responses to user queries.

How to use
To use the program, run the start() function in the main.py file. This will launch a graphical user interface with an image of Sakha. The window will close automatically after 3 seconds.

After the window has closed, the program will listen for voice commands. The user can say "listen to music", "write in my diary", "talk to Sakha", or "exit". If the user says "listen to music", the program will play a song based on the mood stored in the chosen_emotion.txt file. If the user says "write in my diary", the program will open a text file where the user can write a diary entry. If the user says "talk to Sakha", the program will use the OpenAI API to generate a response to the user's query. If the user says "exit", the program will stop running.

File Structure
<li>
main.py: the main program file that launches the GUI and listens for voice commands
chatgptbot.py: the file that handles the OpenAI API and generates responses to user queries
dairy.py: the file that opens a text file where the user can write a diary entry
song1.py: the file that plays a song based on the mood stored in chosen_emotion.txt
chosen_emotion.txt: a text file that stores the user's chosen mood for playing a song
</li>
Dependencies
tkinter
subprocess
os
pyttsx3
speech_recognition
webbrowser
pygame
openai
