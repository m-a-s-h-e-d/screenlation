from TextSpeech import TextSpeech
from tkinter import *
import tkinter
from PIL import Image, ImageTk
import pyttsx3


class SpeechButton:
    def __init__(self, textSpeech, text, root):
        frame = tkinter.Frame(root)
        frame.pack()
        # load speaker image
        self.speakerImage = Image.open("../../_images/speaker.jpg")
        self.speakerImage = self.speakerImage.resize((25, 25), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.speakerImage)
        self.speakerBtn = Button(
            root, image=self.photo, command=lambda: textSpeech.speak(text))
        self.speakerBtn.pack(pady=20)
