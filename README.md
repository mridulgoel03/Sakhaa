# Sakhaa
<h1>Sakhaa your Ai friend</h1>
This code is a chatbot program called "Sakha" that can listen to voice commands and perform tasks such as playing music, writing in a diary, talking to the user, and answering questions.

The program uses several Python libraries, including tkinter, subprocess, os, pyttsx3, speech_recognition, webbrowser, and pygame. It also uses the OpenAI API for generating responses to user queries.

<h3>How to use</h3>
To use the program, run the start() function in the main.py file. This will launch a graphical user interface with an image of Sakha. The window will close automatically after 3 seconds.

<h4>After the window has closed, the program will listen for voice commands.</h4>
The user can say <b>"listen to music"</b>, <b>"write in my diary"</b>, <b>"talk to Sakha"</b>, or <b>"exit"</b>. If the user says <b>"listen to music"</b>, the program will play a song based on the mood stored in the <b>chosen_emotion.txt file</b>. If the user says <b>"write in my diary"</b>, the program will open a text file where the user can write a diary entry. If the user says <b>"talk to Sakha"</b>, the program will use the OpenAI API to generate a response to the user's query. If the user says <b>"exit"</b>, the program will stop running.

<h2><b>File Structure</b></h2>
<li>main.py: the main program file that launches the GUI and listens for voice commands</li>
<li>chatgptbot.py: the file that handles the OpenAI API and generates responses to user queries</li>
<li>dairy.py: the file that opens a text file where the user can write a diary entry</li>
<li>song1.py: the file that plays a song based on the mood stored in chosen_emotion.txt</li>
<li>chosen_emotion.txt: a text file that stores the user's chosen mood for playing a song
</li>
<h2><b>Dependencies</b></h2>

<li>tkinter</li>
<li>subprocess</li>
<li>os</li>
<li>pyttsx3</li>
<li>speech_recognition</li>
<li>webbrowser</li>
<li>pygame</li>
<li>openai</li>
