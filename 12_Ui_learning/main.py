import flet as ft
from src.pages.home_page import HomePage

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Traductor App"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    home_page = HomePage(page=page)

    page.add(home_page.build())

# Ejecutar la aplicación
ft.app(target=main)
