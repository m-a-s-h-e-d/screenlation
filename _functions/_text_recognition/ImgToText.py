from PIL import Image, ImageDraw, ImageFont
import pytesseract, cv2, os
import numpy as np
from pytesseract.pytesseract import Output


# source https://www.askpython.com/python/examples/optical-character-recognition
# using this as placeholder for now (text is recognized better without)
def process_img(img_name):
    #Loading image using OpenCV
    img = cv2.imread(img_name)
    #Preprocessing image
    #Converting to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #creating Binary image by selecting proper threshold
    binary_image = cv2.threshold(gray_image ,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    #Inverting the image
    inverted_bin = cv2.bitwise_not(binary_image)
    #Some noise reduction
    kernel = np.ones((2,2),np.uint8)
    processed_img = cv2.erode(inverted_bin, kernel, iterations = 1)
    processed_img = cv2.dilate(processed_img, kernel, iterations = 1)

    return processed_img


def print_lang_codes():
    langs = pytesseract.get_languages(config='')
    for l in langs:
        print(f"'{l}': ,")


CHI_TRA = "chinese (traditional)"
CHI_TRA_VERT = "chinese (traditional, vertical)"
CHI_SIM = "chinese (simplified)"
CHI_SIM_VERT = "chinese (simplified, vertical)"
JPN = "japanese"
JPN_VERT = "japanese (vertical)"
ENG = "english"
FRA = "french"

lang_options = {
    CHI_TRA: 'chi_tra',
    CHI_TRA_VERT: 'chi_tra_vert',
    CHI_SIM: 'chi_sim',
    CHI_SIM_VERT: 'chi_sim_vert',
    JPN: 'jpn',
    JPN_VERT: 'jpn_vert',
    ENG: 'eng',
    FRA: 'fra',
}

class OCR:
    def __init__(self) -> None:
        self.langs = self.__langoptions__()
        self.selected_lang = 'jp_vert'
    
    def __langoptions__(self):
        tesseract_list = pytesseract.get_languages(config='')
        supported_langs = []
        for k,v in lang_options.items():
            if v in tesseract_list:
                supported_langs.append(k)
        return sorted(supported_langs)
    
    def get_langs(self):
        return self.langs

    def set_lang_idx(self, idx):
        """set the language using the index"""
        lang = None
        try:
            lang = self.langs[idx]
        except IndexError:
            return
        self.set_lang_name(lang)

    def set_lang_name(self, lang_name):
        """set the language using the name of the language"""
        try:
            self.selected_lang = lang_options[lang_name]
        except IndexError:
            print('unknown language name')

    def get_text(self, img):
        return pytesseract.image_to_string(img, lang=self.selected_lang)

    def draw_textboxes(self, img):
        data = pytesseract.image_to_data(img, output_type=Output.DICT)
        print(data)
        for i in range(len(data['level'])):
            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            textbox = ImageDraw.Draw(img)
            textbox.rectangle([(x, y), (x+w, y+h)], fill=None, outline='red') 
        
        img.show()

if __name__ == '__main__':
    img_path = os.path.join(os.path.dirname(__file__), 'fr_test.png')

    print('===================\nUNPROCESSED\n===================')
    # unprocessed test
    ocr = OCR()
    ocr.set_lang_name(FRA)
    ocr.draw_textboxes(Image.open(img_path))