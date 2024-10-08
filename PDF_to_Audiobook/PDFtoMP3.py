import PyPDF2
from gtts import gTTS


# Provide the path to your PDF file and the desired MP3 output filename
pdf_path = 'your_pdf_file.pdf'
mp3_filename = 'audiobook.mp3'


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a PDF"""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text


def text_to_mp3(text: str, mp3_filename: str) -> None:
    """Convert text to an MP3 audiobook"""
    tts = gTTS(text=text, lang='en')
    tts.save(mp3_filename)
    print(f"Audiobook saved as '{mp3_filename}'")


def pdf_to_audiobook(pdf_path: str, mp3_filename: str) -> None:
    """Main function to convert PDF to MP3 audiobook"""
    text = extract_text_from_pdf(pdf_path)
    if text:
        print("Converting PDF to audiobook...")
        text_to_mp3(text, mp3_filename)
    else:
        print("No text found in the PDF.")


# Convert PDF to MP3 audiobook
pdf_to_audiobook(pdf_path, mp3_filename)
