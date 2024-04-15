# speech recognition example
# author: James Campbell
# date: 2015-05-26
# to install pyaudio on osx: brew install portaudio then
# pip install --allow-external pyaudio --allow-unverified pyaudio pyaudio
import speech_recognition as sr  # pip install speechrecognition
from termcolor import colored
r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    # listen for the first phrase and extract it into audio data
    audio = r.listen(source)

try:
    # recognize speech using Google Speech Recognition
    print("You said " + colored(r.recognize(audio), 'yellow'))
    if r.recognize(audio) == 'exit':
        exit('goodbye')
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
