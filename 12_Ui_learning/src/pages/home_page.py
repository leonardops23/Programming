import flet as ft
from src.services.translator import Translator

class HomePage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.translator = Translator()
        self.source_lang = ft.Dropdown(options=[ft.dropdown.Option("es"), ft.dropdown.Option("en")], value="es")
        self.target_lang = ft.Dropdown(options=[ft.dropdown.Option("es"), ft.dropdown.Option("en")], value="en")
        self.input_text = ft.TextField(label="Texto a traducir", multiline=True)
        self.output_text = ft.TextField(label="Traducción", multiline=True, read_only=True)
        self.translate_button = ft.ElevatedButton(text="Traducir", on_click=self.translate_text)

    def translate_text(self, e):
        text = self.input_text.value
        source_lang = self.source_lang.value
        target_lang = self.target_lang.value
        translation = self.translator.translate(text, source_lang, target_lang)
        self.output_text.value = translation
        self.page.update()

    def build(self):
        return ft.Column(
            controls=[
                ft.Text(value="Traductor App", size=24),
                self.input_text,
                ft.Row(controls=[self.source_lang, self.target_lang]),
                self.translate_button,
                self.output_text,
            ]
        )
