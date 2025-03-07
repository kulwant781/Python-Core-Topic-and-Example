import win32com.client

def text_to_speech(file_path):
    try:
        # Open the text file and read its contents
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        # Initialize the speech engine
        speaker = win32com.client.Dispatch("SAPI.SpVoice")

        # Speak the text content
        speaker.Speak(text)

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path of your text file
file_path = "simple.txt"  # Ensure this file exists in the same directory

if __name__ == "__main__":  # Fixed syntax error
    text_to_speech(file_path)
