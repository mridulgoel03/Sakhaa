import os
import random
import time
import pygame
import speech_recognition as sr

def play_songs():
    # Define the file names for each mood
    file_names = {
        'happy': 'happy.txt',
        'sad': 'sad.txt',
        'neutral': 'neutral.txt',
        'romantic': 'relax.txt',
        'angry': 'relax.txt',
        'surprise': 'cool.txt'
    }
    
    # Read the mood from the chosen_emotion.txt file
    with open('chosen_emotion.txt', 'r') as file:
        mood = file.readline().strip().lower()
    
    # Check if the mood entered by the user is valid
    if mood not in file_names:
        print("Invalid mood entered. Please try again.")
        return
    
    # Get the filename for the selected mood
    file_name = file_names[mood]
    
    # Check if the file exists
    if not os.path.exists(file_name):
        print("The file for the selected mood does not exist.")
        return
    
    # Read the songs from the file
    with open(file_name, 'r') as file:
        songs = file.readlines()
    
    # If there are no songs in the file, show a message
    if not songs:
        print("No songs found in the file for the selected mood.")
        return
    
    # Pick a random song from the list of songs
    song = random.choice(songs).strip()
    print("Playing song: ", song)
    
    # Initialize the pygame mixer
    pygame.mixer.init()
    
    # Load the song file
    song = pygame.mixer.Sound(song)
    song_length = song.get_length()

    # Play the song
    pygame.mixer.Sound.play(song)

    # Display the progress bar for the length of the song
    for i in range(int(song_length)):
        progress = int(i / song_length * 100)
        print("\r[{:3d}%]".format(progress), end="")
        time.sleep(1)

        # Use speech recognition to listen for user input
        if i == int(song_length / 12):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("\nDo you want to change the song? Say 'yes' or 'no'.")
                audio = r.listen(source)

            try:
                # Convert the user's speech to text
                user_input = r.recognize_google(audio).lower()
                print("You said: ", user_input)

                # Check if the user wants to change the song
                if user_input == "yes":
                    pygame.mixer.Sound.stop(song)
                    play_songs()
            except sr.UnknownValueError:
                print("Sorry, I could not understand what you said.")

    print("\nSong finished.")

# Call the play_songs function
play_songs()
