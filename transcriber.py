import speech_recognition as sr
# Obtain path to wav file
from os import path
from pydub import AudioSegment


file_name = input("What is the name of the file you want to transcribe? ")

# convert mp3 file to wav                                                       
# sound = AudioSegment.from_mp3("file_name")
# sound.export(file_name, format="wav")

# Transcribe Audio file
AUDIO_FILE = file_name

# Use the audio file as the source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as src:
    audio = r.record(src)
    transciption = "Transciption: " + r.recognize_google(audio)
    print(transciption)

