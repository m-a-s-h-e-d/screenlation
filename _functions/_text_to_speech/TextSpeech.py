import pyttsx3


class TextSpeech:
    def __init__(self):
        self

    def speak(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 180)
        engine.say(text)
        engine.runAndWait()
