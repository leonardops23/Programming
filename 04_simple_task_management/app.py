# task_manager/app.py
from database import create_tables
from auth import Auth
from menu import task_menu

def main():
    """Main function to run the task manager."""
    create_tables()  # Create the tables if they don't exist

    auth = Auth()
    
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            success, message = auth.register(username, password)
            print(message)
        elif choice == '2':
            username = input("Username: ")
            password = input("Password: ")
            success, message = auth.login(username, password)
            print(message)
            if success:
                user = auth.repo.get_user(username)
                task_menu(user_id=user['id'])
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
