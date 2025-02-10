from googletrans import Translator as GoogleTranslator


class Translator:
    def __init__(self):
        # Initialize the Google Translate client
        self.translator = GoogleTranslator()
    
    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """
        Translates text from the source language to the target language using Google Translate.

        Args:
            text (str): The text to translate.
            source_lang (str): The source language code (e.g., "en" for English).
            target_lang (str): The target language code (e.g., "es" for Spanish).

        Returns:
            str: The translated text or an error message if the translation fails.
        """
        try:
            translated = self.translator.translate(text, src=source_lang, dest=target_lang)
            return translated.text
        except Exception as e:
            return f"Translation Error: {str(e)}"
