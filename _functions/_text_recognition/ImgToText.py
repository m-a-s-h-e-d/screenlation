from PIL import Image
import pytesseract, cv2
import numpy as np


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


def get_text(img,lang_code):
    return pytesseract.image_to_string(img, lang=lang_code)


def print_lang_codes():
    langs = pytesseract.get_languages(config='')
    for l in langs:
        print(f"'{l}': ,")
    

if __name__ == '__main__':
    img_name = 'jp_test.png'

    # print('===================\nPROCESSED\n===================')
    # # processing image test 
    # clean_img = process_img(img_name)
    # print(pytesseract.image_to_string(clean_img))


    print('===================\nUNPROCESSED\n===================')
    # unprocessed test
    unprocessed_img = Image.open(img_name)
    print(pytesseract.image_to_string(unprocessed_img, lang='jpn_vert'))
