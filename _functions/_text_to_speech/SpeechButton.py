from TextSpeech import TextSpeech
from tkinter import *
import tkinter
from PIL import Image, ImageTk
import pyttsx3


class SpeechButton:
    def __init__(self, text_speech, text, root):
        frame = tkinter.Frame(root)
        frame.pack()
        # load speaker image
        self.speaker_image = Image.open("../../_images/speaker.jpg")
        self.speaker_image = self.speaker_image.resize(
            (25, 25), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.speaker_image)
        self.speaker_btn = Button(
            root, image=self.photo, command=lambda: text_speech.speak(text))
        self.speaker_btn.pack()
