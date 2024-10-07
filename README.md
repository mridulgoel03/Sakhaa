# Sakhaa: Your AI Friend

Sakhaa is a chatbot program that listens to voice commands and performs various tasks such as playing music, writing in a diary, talking to the user, and answering questions. It leverages several Python libraries and the OpenAI API to enhance user interaction.

## Features

- **Voice Command Recognition**: Responds to specific voice commands.
- **Music Playback**: Plays a song based on the mood stored in `chosen_emotion.txt`.
- **Diary Entry**: Allows users to write diary entries.
- **Chat with Sakhaa**: Generates responses to user queries using the OpenAI API.
- **Exit Command**: Gracefully terminates the program.

## How to Use

1. **Run the Program**: Execute the `start()` function in the `main.py` file. This will launch a graphical user interface (GUI) with an image of Sakhaa. 
2. **Automatic Closure**: The GUI window will automatically close after 3 seconds.
3. **Voice Commands**: After the window closes, the program will listen for voice commands. You can say:
   - **"listen to music"**: Plays a song based on your mood.
   - **"write in my diary"**: Opens a text file for diary entries.
   - **"talk to Sakha"**: Engages with the OpenAI API for responses.
   - **"exit"**: Stops the program.


## File Structure

```
- `main.py`              # Main program file that launches the GUI and listens for voice commands
- `chatgptbot.py`        # Handles OpenAI API and generates responses to user queries
- `diary.py`             # Opens a text file for writing diary entries
- `song1.py`             # Plays a song based on the mood stored in `chosen_emotion.txt`
- `chosen_emotion.txt`    # Stores the user's chosen mood for playing a song
```


## Dependencies

To run `Sakhaa`, ensure you have the following Python libraries installed:

- `tkinter`
- `subprocess`
- `os`
- `pyttsx3`
- `speech_recognition`
- `webbrowser`
- `pygame`
- `openai`

## Installation

To install the dependencies, you can use pip:

```bash
pip install tkinter pyttsx3 SpeechRecognition pygame openai
```

## Contributing

If you would like to contribute to `Sakhaa`, follow these steps:

1. **Fork the repository**: Click on the "Fork" button at the top right corner of the page.
2. **Create your feature branch**: 
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. **Commit your changes**: 
   ```bash
   git commit -m "Add some feature"
   ```
4. **Push to the branch**: 
   ```bash
   git push origin feature/YourFeatureName
   ```
5. **Open a pull request**: Go to the original repository and click on the "Pull Requests" tab, then click on "New Pull Request."

Your contributions are welcome! Whether it’s fixing bugs, improving documentation, or adding features, every bit helps!
