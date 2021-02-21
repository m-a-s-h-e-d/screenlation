import tkinter
from tkinter.constants import COMMAND
from numpy import common_type
import pytesseract

# maps the language code to the displayed name of the language
# CODE_NAME_MAPPING = {
#     'afr': 'Afrikaans',
#     'amh': 'Amharic',
#     'ara': 'Arabic',
#     'aze': 'Azerbaijani',
#     'aze_cryl': 'Azerbaijani(Cryllic)',
#     'bel': 'Belarusian',
#     'ben': 'Bengali',
#     'bul': 'Bulgarian',
#     'cat': 'Catalan',
#     'ces': 'Czech',
#     'chi_sim': 'Simplified Chinese(horizontal)',
#     'chi_sim_vert': 'Simplified Chinese(vertical)',
#     'chi_tra': 'Traditional Chinese(horizontal)',
#     'chi_tra_vert': 'Traditional Chinese(horizontal)',
#     'cym': 'Welsh',
#     'dan': 'Danish',
#     'deu': 'German',
#     'ell': 'Greek',
#     'eng': 'English',
#     'epo': 'Esperanto',
#     'est': 'Estonian',
#     'eus': 'Basque',
#     'fas': 'Persian',
#     'fil': 'Filipino',
#     'fin': 'Finnish',
#     'fra': 'French',
#     'gle': 'Irish',
#     'glg': 'Galician',
#     'guj': 'Gujarati',
#     'hat': 'Haitian Creole',
#     'heb': 'Hebrew',
#     'hin': 'Hindi',
#     'hrv': 'Crotian',
#     'hun': 'Hungarian',
#     'hye': 'Armenian',
#     'iku': 'Inuktitut',
#     'ind': 'Indonesian',
#     'isl': 'Icelandic',
#     'ita': 'Italian',
#     'jpn': 'Japanese(horizontal)',
#     'jpn_vert': 'Japanese(vertical)',
#     'kan': 'Kannada',
#     'kat': 'Georgian',
#     'kat_old': 'Georgian(old)',
#     'kaz': 'Kazakh',
#     'khm': 'Khmer',
#     'kor': 'Korean',
#     'lao': 'Lao',
#     'lav': 'Latvian',
#     'lit': 'Lituanian',
#     'msa': 'Malay',
#     'pol': 'Polish',
#     'rus': 'Russian',
#     'slv': 'Slovak',
#     'spa': 'Spanish',
#     'swa': 'Swahili',
#     'swe': 'Swedish',
#     'tha': 'Thai',
#     'tir': 'Tigurian',
#     'ton': 'Tongan',
#     'tur': 'Turkish',
#     'ukr': 'Ukranian',
#     'urd': 'Urdu',
#     'vie': 'Vietnamese'
# }

class ScrollBarMenu:
    def __init__(self, item_list, root):
        frame = tkinter.Frame(root)
        frame.pack()
        self.items = item_list
        self.scrollbar = tkinter.Scrollbar(root)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.menu_box = tkinter.Listbox(root, yscrollcommand = self.scrollbar.set)
        for i in range(0, len(item_list)):
            self.menu_box.insert(i, item_list[i])
        self.menu_box.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.scrollbar.config(command = self.menu_box.yview)

    def get_selection(self):
        print(self.menu_box.get(tkinter.ANCHOR))
        
    
    

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('screenlation')
    root.geometry('400x480')
    menu = ScrollBarMenu([1, 2, 3], root)
    menu.menubox.bind("<<ListboxSelect>>", )
    root.mainloop()