import speech_recognition as sr
import os
import subprocess

# Initialize the recognizer
r = sr.Recognizer()

def listen_directly():
    while(1):
        doc = ""
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio_data = r.listen(source)
                text = r.recognize_google(audio_data)
                doc = doc + text
                print(text)
                if text == 'Done':
                    break
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occured")
    return doc

def listen_file(path):
    doc = ""
    print(path)
    # cmdline = ['avconv','-i',path,'-vn','-f','wav','test.wav']
    os.system('ffmpeg -i {} {}'.format(path,path.replace('mp4','mp3')))
    try:
        with sr.AudioFile(path) as source:
            r.adjust_for_ambient_noise(source, duration=0.5)   
            audio_data = r.listen()
            text = r.recognize_google(audio_data)
            doc = doc + text
            print(text)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")
    return doc

path = r'C:\SP\workspaces\vscode1\documenter\test.mp4'

if path:
    doc = listen_file(path)
else:
    doc = listen_directly()

print(doc)
