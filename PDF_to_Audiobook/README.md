## PDF to Audiobook Converter
This Python program converts a PDF file into an audiobook (MP3 format).   
It extracts text from the PDF and uses Google's Text-to-Speech (gTTS) API to generate the audio file.   
The resulting MP3 can be played on any compatible device, turning your PDFs into spoken-word audiobooks!

### Features
- Extracts text from a PDF file.
- Converts the extracted text into an MP3 audiobook.
- Saves the MP3 file for later use.
- Supports multiple languages (using Google Text-to-Speech).

### Requirements
To run this program, you will need:

- Python 3.x
- PyPDF2 library for PDF text extraction.
- gTTS (Google Text-to-Speech) library for converting text to speech.
- Install the required libraries using pip:  
`pip install PyPDF2 gtts`

### How to Use
1. Prepare your PDF:    
Place the PDF file that you want to convert in the same directory as the script (or specify its path).  
2. Run the Script:   
In the script, provide the path to your PDF file and the desired name of the output MP3 file.

Example:  
`pdf_path = 'your_pdf_file.pdf'`  
`mp3_filename = 'audiobook.mp3'`  


### Execute the script: 

1. Run the Python script to convert the PDF to an audiobook:  
`python pdf_to_audiobook.py`

2. Enjoy your audiobook:   
The resulting MP3 file will be saved in the specified directory.   
You can now listen to the audiobook on any MP3 player or device.  


### Customization
- You can change the speaking speed, volume, or language of the output by modifying the parameters in the gTTS function.
= For other languages, change 'en' in the line tts = gTTS(text=text, lang='en') to your desired language code (e.g., 'fr' for French or 'es' for Spanish).

### Known Limitations
- The program works only for PDFs that contain selectable text (i.e., not scanned images).
- An internet connection is required for using the Google Text-to-Speech service (gTTS).


### License
This project is licensed under the MIT License.
