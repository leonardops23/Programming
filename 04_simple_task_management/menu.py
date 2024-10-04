# task_manager/menu.py
from task_repository import TaskRepository

def task_menu(user_id):
    """Menu for managing tasks."""
    repo = TaskRepository()
    
    while True:
        print("\nTask Manager")
        print("1. Add a new task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Task title: ")
            priority = input("Priority (low, medium, high): ")
            due_date = input("Due date (YYYY-MM-DD): ")
            repo.add_task(user_id, title, priority, due_date)
            print("Task added successfully!")
        elif choice == '2':
            tasks = repo.get_tasks(user_id)
            for task in tasks:
                print(f"ID: {task[0]}, Title: {task[2]}, Priority: {task[3]}, Due Date: {task[4]}, Status: {task[5]}")
        elif choice == '3':
            task_id = int(input("Task ID to mark as complete: "))
            repo.update_task_status(task_id, 'complete')
            print("Task marked as complete!")
        elif choice == '4':
            task_id = int(input("Task ID to delete: "))
            repo.delete_task(task_id)
            print("Task deleted successfully!")
        elif choice == '5':
            break
        else:
            print("Invalid option. Try again.")
