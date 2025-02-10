import flet as ft
from src.services.translator import Translator


class HomePage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.translator = Translator()
        self.input_text = ft.TextField(
            label="Texto a Traducir",
            min_lines=3,
            max_lines=5,
            expand=True,
            multiline=True
        )
        self.output_text = ft.TextField(
            label="Translation",
            multiline=True,
            min_lines=3,
            max_lines=5,
            expand=True,
            read_only=True
        )
        self.language_from = ft.Dropdown(
            label="Source Language",
            options=[
                ft.dropdown.Option("es"),
                ft.dropdown.Option("en"),
                ft.dropdown.Option("fr"),
                ft.dropdown.Option("it"),
                ft.dropdown.Option("de"),
            ],
            value="es",
            width=150,
        )
        self.language_to = ft.Dropdown(
            label="Target Language",
            options=[
                ft.dropdown.Option("es"),
                ft.dropdown.Option("en"),
                ft.dropdown.Option("fr"),
                ft.dropdown.Option("it"),
                ft.dropdown.Option("de"),
            ],
            value="en",
            width=150,
        )
        self.translate_button = ft.ElevatedButton(text="Translate", on_click=self.click_translate)
        self.icon_micro = ft.Icon(name=ft.Icons.MULTITRACK_AUDIO)
        self.icon_camara = ft.Icon(name=ft.Icons.CAMERA_ALT)
        self.icon_menu = ft.Icon(name=ft.Icons.HISTORY)

    def click_translate(self, e):
        text = self.input_text.value
        source = self.language_from.value
        target = self.language_to.value
        translated = self.translator.translate(text, source, target)
        self.output_text.value = translated
        self.page.update()

    def history(self, e):
        self.page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Selected: {e.control.text}"),
                                             open=True))

    def build(self):
        return ft.Column(
            controls=[
                ft.Text(value="Traductor", size=24),
                self.icon_menu,
                ft.Row(
                    controls=[
                        self.language_from,
                        ft.Icon(name=ft.icons.ARROW_FORWARD, color=ft.colors.BLUE),
                        self.language_to,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                self.input_text,
                ft.Row(
                    controls=[
                        self.icon_micro,
                        self.icon_camara,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                self.translate_button,
                self.output_text,
            ]
        )
