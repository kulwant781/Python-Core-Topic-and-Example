# Import the required module for text-to-speech conversion
import win32com.client
import voice  # Importing the voice module

# Initialize the speech engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    print("Enter the word you want the computer to speak (or type 'start' to end): ")
    user_input = input()
    
    if user_input.lower() == "start":
        break

    speaker.Speak(user_input)

# Call function from voice.py
file_path = "simple.txt"
voice.text_to_speech(file_path)
