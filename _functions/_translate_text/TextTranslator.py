from deep_translator import (GoogleTranslator, DeepL)


class TextTranslator:
    def __init__(self):
        self

    def get_google_supported_language(self):
        return GoogleTranslator.get_supported_languages()

    def google_translate(self, target, original_text):
        translated_text = GoogleTranslator(
            source='auto', target=target).translate(text=original_text)
        return translated_text

    # maybe unnecessary
    def google_translate_paragraph(self, target, original_texts):
        translated_text = GoogleTranslator(
            source='auto', target=target).translate_batch(original_texts)
        translated_paragraph = '. '.join(translated_text)
        return translated_paragraph
