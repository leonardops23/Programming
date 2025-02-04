import requests

class Translator:
    def __init__(self):
        self.base_url = "https://libretranslate.com/translate"

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        payload = {
            "q": text,
            "source": source_lang,
            "target": target_lang,
            "format": "text"
        }
        response = requests.post(self.base_url, json=payload)
        if response.status_code == 200:
            return response.json().get("translatedText", "")
        else:
            return f"Error: {response.status_code}"
