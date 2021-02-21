from tkinter import Tk
import pytesseract

# maps the language code to the displayed name of the language
CODE_NAME_MAPPING = {
    'afr': 'Afrikaans',
    'amh': 'Amharic',
    'ara': 'Arabic',
    'aze': 'Azerbaijani',
    'aze_cryl': 'Azerbaijani(Cryllic)',
    'bel': 'Belarusian',
    'ben': 'Bengali',
    'bul': 'Bulgarian',
    'cat': 'Catalan',
    'ces': 'Czech',
    'chi_sim': 'Simplified Chinese(horizontal)',
    'chi_sim_vert': 'Simplified Chinese(vertical)',
    'chi_tra': 'Traditional Chinese(horizontal)',
    'chi_tra_vert': 'Traditional Chinese(horizontal)',
    'cym': 'Welsh',
    'dan': 'Danish',
    'deu': 'German',
    'ell': 'Greek',
    'eng': 'English',
    'epo': 'Esperanto',
    'est': 'Estonian',
    'eus': 'Basque',
    'fas': 'Persian',
    'fil': 'Filipino',
    'fin': 'Finnish',
    'fra': 'French',
    'gle': 'Irish',
    'glg': 'Galician',
    'guj': 'Gujarati',
    'hat': 'Haitian Creole',
    'heb': 'Hebrew',
    'hin': 'Hindi',
    'hrv': 'Crotian',
    'hun': 'Hungarian',
    'hye': 'Armenian',
    'iku': 'Inuktitut',
    'ind': 'Indonesian',
    'isl': 'Icelandic',
    'ita': 'Italian',
    'jpn': 'Japanese(horizontal)',
    'jpn_vert': 'Japanese(vertical)',
    'kan': 'Kannada',
    'kat': 'Georgian',
    'kat_old': 'Georgian(old)',
    'kaz': 'Kazakh',
    'khm': 'Khmer',
    'kor': 'Korean',
    'lao': 'Lao',
    'lav': 'Latvian',
    'lit': 'Lituanian',
    'msa': 'Malay',
    'pol': 'Polish',
    'rus': 'Russian',
    'slv': 'Slovak',
    'spa': 'Spanish',
    'swa': 'Swahili',
    'swe': 'Swedish',
    'tha': 'Thai',
    'tir': 'Tigurian',
    'ton': 'Tongan',
    'tur': 'Turkish',
    'ukr': 'Ukranian',
    'urd': 'Urdu',
    'vie': 'Vietnamese'
}


class LanguageMenu:
    def __init__(self) -> None:
        self.lang_dict = self.__initlangs__()
        self.selected_lang = 'fra'
    
    def __initlangs__(self) -> dict:
        tesseract_list = pytesseract.get_languages(config='')
        supported_langs = {}
        for item in tesseract_list:
            if item in CODE_NAME_MAPPING:
                supported_langs[item] = CODE_NAME_MAPPING[item]
        # sort languages into alphabetical order based on the name
        supported_langs = sorted(supported_langs.items(), key=lambda item:item[1])

        return supported_langs
    
    def get_lang_names(self) -> list:
        return list(self.lang_dict.values())
    
    def get_lang_code(self, idx) -> str:
        """
        get the language code of the available languages based on its indexed positon
        return None if the index is out of bound
        """
        result = None
        try:
            result = list(self.lang_dict)[idx]
        except IndexError:
            pass
        finally:
            return result
    
    def make_selection(idx):
        pass


class ScrollBarMenu:
    def __init__(self, item_list):
        self.items = item_list
    
    

if __name__ == '__main__':
    pass