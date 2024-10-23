import tkinter as tk
import json
from tkinter import messagebox


def open_task_manager(username):
    # Main window of the task manager
    root = tk.Tk()
    root.title(f"Task Manager - {username}")
    root.geometry("400x400")

    # Task list
    task_list = []

    # Function to load user's tasks
    def load_tasks():
        try:
            with open(f"{username}_tasks.json", "r") as file:
                loaded_tasks = json.load(file)
                for task in loaded_tasks:
                    task_listbox.insert(tk.END, task)
                    task_list.append(task)
        except FileNotFoundError:
            pass  # If no file is found, do nothing

    # Function to save user's tasks
    def save_tasks():
        with open(f"{username}_tasks.json", "w") as file:
            json.dump(task_list, file)

    # Function to add a task
    def add_task():
        task = entry_task.get()
        if task:
            task_listbox.insert(tk.END, task)
            task_list.append(task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    # Function to delete the selected task
    def delete_task():
        try:
            selected_task_index = task_listbox.curselection()[0]
            task_listbox.delete(selected_task_index)
            task_list.pop(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to delete.")

    # Function to mark a task as completed
    def mark_task_completed():
        try:
            selected_task_index = task_listbox.curselection()[0]
            task = task_listbox.get(selected_task_index)
            task_listbox.delete(selected_task_index)
            task_listbox.insert(tk.END, f"{task} (completed)")
            task_list[selected_task_index] = f"{task} (completed)"
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to mark as completed.")

    # UI Widgets
    entry_task = tk.Entry(root, width=35)
    entry_task.pack(pady=10)

    btn_add_task = tk.Button(root, text="Add Task", width=15, command=add_task)
    btn_add_task.pack(pady=5)

    btn_delete_task = tk.Button(root, text="Delete Task", width=15, command=delete_task)
    btn_delete_task.pack(pady=5)

    btn_mark_completed = tk.Button(root, text="Mark as Completed", width=20, command=mark_task_completed)
    btn_mark_completed.pack(pady=5)

    task_listbox = tk.Listbox(root, width=35, height=10)
    task_listbox.pack(pady=10)

    btn_save_tasks = tk.Button(root, text="Save Tasks", width=15, command=save_tasks)
    btn_save_tasks.pack(pady=5)

    # Load tasks when starting
    load_tasks()

    # Run the main window
    root.mainloop()
