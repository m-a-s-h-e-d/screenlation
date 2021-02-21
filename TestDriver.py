from tkinter import *
from PIL import Image, ImageTk
import pyttsx3
# from _functions._text_to_speech.TextSpeech import TextSpeech
# from _functions._text_to_speech.SpeechButton import SpeechButton
from _functions._translate_text.TextTranslator import TextTranslator
from _functions._text_recognition.Application import ScrollBarMenu

textTranslator = TextTranslator()
root = Tk()
root.title('Screenlation')
root.geometry("1000x630")


greeting = Label(text="Screenlation")
greeting.pack()

# textSpeech = TextSpeech()
# speaker1 = SpeechButton(textSpeech, "Hello", root)
# speaker2 = SpeechButton(textSpeech, "Hello", root)
# textSpeech.speak("hello")


# frame for input, output
text_box_frame = Frame(root)
text_box_frame.pack()


def translate():
    input_text = input_box.get(1.0, END)
    target_language = output_scroll_bar_menu.get_selection()
    translated = textTranslator.google_translate(
        target_language, input_text)
    output_box.delete(1.0, END)
    output_box.insert(END, translated)


input_box = Text(text_box_frame, width=50, height=10)
input_box.config(highlightbackground="black")
translate_btn = Button(text_box_frame,
                       text="translate",
                       width=10,
                       height=2,
                       command=translate
                       )
output_box = Text(text_box_frame, width=50, height=10)
output_box.config(highlightbackground="black")
input_box.pack(pady=20)
translate_btn.pack()
output_box.pack(pady=17)
output_scroll_bar_menu = ScrollBarMenu(
    textTranslator.get_google_supported_language(), root)


# textTranslator = TextTranslator()
# print(textTranslator.get_google_supported_language())

# para = ["Hello, it's me", "How are you?"]
# print(textTranslator.google_translate('vi', "Sunset is the time of day when our sky meets the outer space solar winds. There are blue, pink, and purple swirls, spinning and twisting, like clouds of balloons caught in a whirlwind. The sun moves slowly to hide behind the line of horizon, while the moon races to take its place in prominence atop the night sky. People slow to a crawl, entranced, fully forgetting the deeds that must still be done. There is a coolness, a calmness, when the sun does set."))

root.mainloop()
