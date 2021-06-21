import os
import textract
import gtts
import playsound

def document_reader(filename):
    text = textract.process(filename)
    # print(text)
    return str(text)
    
def reader(message):
    language = 'en'
    myobj = gtts.gTTS(text=message, lang=language, slow=False)
  
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("welcome.mp3")
    playsound.playsound("welcome.mp3")
# Playing the converted file

data = document_reader(r'CheckMovieStory.docx')
reader(data)
