import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import pyaudio  # to install pyaudio on osx: brew install portaudio then pip install --allow-external pyaudio --allow-unverified pyaudio pyaudio
import speech_recognition as sr  # pip install speechrecognition
from termcolor import colored
import pyaudio
import wave

r = sr.Recognizer()
with sr.Microphone() as source:  # use the default microphone as the audio source
    audio = r.listen(source)

CHUNK = 1024
FORMAT = pyaudio.paInt16  # paInt8
CHANNELS = 1
RATE = 44100  # sample rate
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
)  # buffer

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)  # 2 bytes(16 bits) per channel
wf = wave.open("temp.wav", "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b"".join(frames))
wf.close()
print("* done recording")
stream.stop_stream()
stream.close()
p.terminate()
spf = wave.open("temp.wav", "r")
signal = spf.readframes(-1)
signal = np.fromstring(signal, "Int16")
plt.figure(1)
plt.title("Signal Wave...")
plt.plot(signal)
plt.show()
exit()
