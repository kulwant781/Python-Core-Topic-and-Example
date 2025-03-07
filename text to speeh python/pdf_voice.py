# importing the modules
import PyPDF2
import pyttsx3

# Open the PDF file
with open("newdd.pdf", "rb") as path:
    # Create a PdfReader object
    pdf_reader = PyPDF2.PdfReader(path)  # Use PdfReader instead of PdfFileReader

    # Specify the page number (0-based index)
    page_number = 2  # 25th page (0-indexed)

    if page_number < len(pdf_reader.pages):
        # Extract text from the specified page
        text = pdf_reader.pages[page_number].extract_text()  # Use pages[index]
        
        # Initialize text-to-speech engine
        speak = pyttsx3.init()
        speak.say(text)
        speak.runAndWait()
    else:
        print("Error: Page number out of range.")
