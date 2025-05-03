import os
import flet as ft
import json

FILE_USERS = "users.json"


def load_users():
    """
    Carga los usuarios desde un archivo
    """
    if not os.path.exists(FILE_USERS):
        return {}
    
    with open(FILE_USERS, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}


def save_users(users):
    """Guarda los usuarios en un archivo"""
    with open(FILE_USERS, "w") as file:
        json.dump(users, file, indent=4) # indent=4 para que el archivo tenga un formato mas legible


def main(page: ft.Page):
    page.title = "Sistema de Login y registro"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_with = 400
    page.window_height = 600
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    users = load_users()

    current_user = None

    # mensajes
    message = ft.Text("", color=ft.colors.RED, text_align=ft.TextAlign.CENTER) # mensaje de error
    success_message = ft.Text("", color=ft.colors.GREEN, text_align=ft.TextAlign.CENTER) # mensaje de exito

    login_view = ft.Column(
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    register_view = ft.Column(
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # campos de inicio de sesion
    email_login = ft.TextField(
        label="Correo Electronico",
        border=ft.InputBorder.UNDERLINE,
        width=200,
        autofocus=True,
    )

    password_login = ft.TextField(
        label="Contraseña",
        border=ft.InputBorder.UNDERLINE,
        width=200,
        autofocus=True,
        password=True,
        can_reveal_password=True,
    )

    # home view
    home_view = ft.Column(
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # campos de registro
    name_register = ft.TextField(
        label="Nombre",
        border=ft.InputBorder.UNDERLINE,
        width=200,
        autofocus=True,
    )

    email_register = ft.TextField(
        label="Correo Electronico",
        border=ft.InputBorder.UNDERLINE,
        width=200,
        autofocus=True,
    )

    password_register = ft.TextField(
        label="Contraseña",
        border=ft.InputBorder.UNDERLINE,
        width=200,
        autofocus=True,
        password=True,
        can_reveal_password=True,
    )

    confirm_password_register = ft.TextField(
        label="Confirmar Contraseña",
        border=ft.InputBorder.UNDERLINE,
        width=200,
        autofocus=True,
        password=True,
        can_reveal_password=True,
    )


    def clear_fields():
        """Limpia los campos de texto"""
        email_login.value = ""
        password_login.value = ""
        name_register.value = ""
        email_register.value = ""
        password_register.value = ""
        confirm_password_register.value = ""


    def show_login():
        """Muestra la vista de inicio de sesion"""
        page.clean()
        message.value = ""
        success_message.value = ""
        login_view.controls = [
            ft.Text("Iniciar Sesion", size=24, weight=ft.FontWeight.BOLD),
            email_login,
            password_login,
            message,
            ft.ElevatedButton(
                text="Iniciar Sesion",
                width=200,
                on_click=handle_login,
            ),
            ft.TextButton(
                text="¿No tienes una cuenta? Registrate",
                on_click=lambda _: show_register(),
            )
        ]

        page.add(login_view)
        page.update()

    def show_register():
        """Muestra la vista de registro"""
        page.clean() # limpia la pantalla
        message.value = ""
        success_message.value = ""
        register_view.controls = [
            ft.Text("Registrarse", size=24, weight=ft.FontWeight.BOLD),
            name_register,
            email_register,
            password_register,
            confirm_password_register,
            message,
            success_message,
            ft.ElevatedButton(
                text="Registrarse",
                width=200,
                on_click=handle_register,
            ),
            ft.TextButton(
                text="¿Tienes una cuenta? Inicia sesión",
                on_click=lambda _: show_login(),
            )
        ]

        page.add(register_view)
        page.update()


    def show_home():
        """
        Muestra la vista del usuario despues de hacer sesion
        """
        page.clean()
        home_view.controls = [
            ft.Text("Inicio", size=24, weight=ft.FontWeight.BOLD),
            ft.Text(f"Bienvenido {current_user}", size=20),
            ft.TextButton(
                text="Cerrar Sesion",
                on_click=lambda _: show_login(),
            )
        ]

        page.add(home_view)
        page.update()


    def handle_login(e):
        """Maneja el inicio de sesion"""
        nonlocal current_user # indica que se va a usar la variable global

        email = email_login.value
        password = password_login.value

        if not email or not password:
            message.value = "Por favor, completa todos los campos"
            page.update()
            return

        if email not in users or users[email]["password"] != password:
            message.value = "Correo Electronico o Contraseña incorrectos"
            page.update()
            return

        current_user = email
        clear_fields()
        show_home()

    show_login()


    def handle_register(e):
        """Maneja el registro"""
        nonlocal current_user # indica que se va a usar la variable global

        name = name_register.value
        email = email_register.value
        password = password_register.value
        confirm_password = confirm_password_register.value

        if not name or not email or not password or not confirm_password:
            message.value = "Por favor, completa todos los campos"
            page.update()
            return

        if password != confirm_password:
            message.value = "Las contraseñas no coinciden"
            page.update()
            return

        users[email] = {
            "name": name,
            "password": password,
        }
        save_users(users)
        clear_fields()
        show_login()

ft.app(main)
