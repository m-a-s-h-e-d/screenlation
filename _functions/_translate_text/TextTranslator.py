from deep_translator import (GoogleTranslator, DeepL)


class TextTranslator:
    def __init__(self):
        self

    def get_google_supported_language(self):
        return GoogleTranslator.get_supported_languages()

    def google_translate(self, target, originalText):
        translatedText = GoogleTranslator(
            source='auto', target=target).translate(text=originalText)
        return translatedText

    # maybe unnecessary
    def google_translate_paragraph(self, target, originalTexts):
        translatedText = GoogleTranslator(
            source='auto', target=target).translate_batch(originalTexts)
        translatedParagraph = '. '.join(translatedText)
        return translatedParagraph
