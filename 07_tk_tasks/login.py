import json
from tkinter import messagebox
import hashlib
import tkinter as tk


def login():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        try:
            with open("users.json", "r") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if username in users and users[username] == hashed_password:
            messagebox.showinfo("Login", "!successful login")
            login_window.destroy()
            open_task_manager(username)
        else:
            messagebox.showwarning("Error", "incorrect user or password")
    else:
        messagebox.showwarning("Error", "Please complete all fields.")


def register():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        try:
            with open("users.json", "r") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}

        if username in users:
            messagebox.showwarning("Error", "User already exists")
        else:
            hashed_password = hashlib.sha3_256(password.encode()).hexdigest()
            users[username] = hashed_password
            with open("users.json", "w") as file:
                json.dump(users, file)
            messagebox.showinfo("Register", "!successful Register")
    else:
        messagebox.showwarning("Error", "Please complete all fields.")


# drow_app
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("400x360")

tk.Label(login_window, text="User: ").pack(pady=5)
entry_username = tk.Entry(login_window)
entry_username.pack(pady=5)

tk.Label(login_window, text="Password").pack(pady=5)
entry_password = tk.Entry(login_window, show="*")
entry_password.pack(pady=5)

btn_login = tk.Button(login_window, text="Login", command=login)
btn_login.pack(pady=10)

btn_register = tk.Button(login_window, text="Register")
btn_register.pack(pady=3)

login_window.mainloop()
