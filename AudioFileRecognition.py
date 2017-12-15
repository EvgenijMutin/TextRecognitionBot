from os import path
import speech_recognition as sr

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    print("Text in you .wav file: " + "\n" + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))