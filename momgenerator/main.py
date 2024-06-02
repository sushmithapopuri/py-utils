from transcripter import generate_transcript
from mom import summarize
from mom2 import generate_summary

#Provide the full path of the mp4 File 

file_names = ['test2.mp4','transcript2.txt','mom2.txt']
transcript = generate_transcript(file_names[0]) #Generate transcript from meeting Recording

#Save Generated transcript to a file
with open(file_names[1],'w+') as f:
    f.write(transcript)

mom = summarize(transcript) # Generate MOM from transcript

#Save Generated MOM to a file
with open(file_names[2],'w+') as f:
    f.write(''.join(mom))
