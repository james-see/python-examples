# speech recognition example
# author: James Campbell
# date: 2015-05-26
import pyaudio # to install pyaudio on osx: brew install portaudio then pip install --allow-external pyaudio --allow-unverified pyaudio pyaudio
import speech_recognition as sr # pip install speechrecognition
from termcolor import colored
r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

try:
    print("You said " + colored(r.recognize(audio),'yellow'))    # recognize speech using Google Speech Recognition
    if r.recognize(audio) == 'exit':
    	exit('goodbye') 
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
