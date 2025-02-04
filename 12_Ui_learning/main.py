import flet as ft
from src.pages.home_page import HomePage

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Traductor App"
    page.padding = 20

    # Mostrar la página principal
    home_page = HomePage(page)
    page.add(home_page.build())

# Ejecutar la aplicación
ft.app(target=main)
