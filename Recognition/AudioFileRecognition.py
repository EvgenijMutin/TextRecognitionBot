from os import path
import speech_recognition as sr


def audioFileRecognition(afile):
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), afile)
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    try:
        answerForAudioFile = "Text in you file: " + "\n" + r.recognize_google(audio)
    except sr.UnknownValueError:
        answerForAudioFile = "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        answerForAudioFile = "Could not request results from Google Speech Recognition service; {0}".format(e)

    return answerForAudioFile
