from fileinput import filename
import subprocess
import speech_recognition as sr
from datetime import datetime
import sys

#Generate Test transcript from the mp4 video ( meeting recording) using ffmpeg and speech rcognition
def generate_transcript(file_name):
    aud = file_name.split('.mp4')[0] + '_'+ str(datetime.now().microsecond) + '.wav'
    # Command to convert video to Audio
    command = "ffmpeg -i {} -ab 160k -ac 2 -ar 44100 -vn {}".format(file_name,aud)
    subprocess.call(command, shell=True)

    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Open the audio file and generate transcript
    with sr.AudioFile(aud) as source:
        audio_text = r.record(source)
    # Recognize the speech in the audio with EN mode
    text = r.recognize_google(audio_text,language= 'en-US')
    return text