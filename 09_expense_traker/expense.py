from colorama import Fore, Style
import json
import os
from collections import defaultdict


class Expense:
    """
    Represents an expense with a name, category, and amount.

    Attributes:
        name (str): The name of the expense.
        category (str): The category of the expense.
        ammount (float): The amount of the expense.
    """
    def __init__(self, name, category, ammount):
        self.name = name
        self.category = category
        self.ammount = ammount

    def __repr__(self):
        return f"Expense: {self.name} - {self.category} - {self.ammount}"


def calculate_totals() -> None:
    """
    Calculate and display the total expenses by category and the overall total.

    Reads the data from 'data.json' file and computes the sum of amounts for each category.
    Also displays the total amount of all expenses.

    If the file does not exist or is corrupted, appropriate error messages are displayed.
    """
    save_data = "data.json"

    if not os.path.exists(save_data):
        print(f"{Fore.RED}No data file found!{Style.RESET_ALL}")
        return

    try:
        # Read data from the JSON file
        with open(save_data, "r") as file:
            data_list = json.load(file)

        if not data_list:
            print(f"{Fore.YELLOW}No expenses recorded yet.{Style.RESET_ALL}")
            return

        # Compute totals by category
        totals_by_category = defaultdict(float)
        total_expenses = 0

        for entry in data_list:
            category = entry.get("category", "Unknown")  # Handle missing categories
            amount = entry.get("amount", 0)  # Handle missing amounts
            totals_by_category[category] += amount
            total_expenses += amount

        # Display results
        print(f"\n{Fore.BLUE}Expense Summary:{Style.RESET_ALL}")
        for category, total in totals_by_category.items():
            print(f"  {Fore.CYAN}{category}: ${total:.2f}{Style.RESET_ALL}")

        print(f"\n{Fore.GREEN}Total Expenses: ${total_expenses:.2f}{Style.RESET_ALL}")

    except json.JSONDecodeError:
        print(f"{Fore.RED}Error reading data file. File may be corrupted.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}")


def get_name_expense() -> str:
    """
    Prompt the user to enter the name of the expense.

    Returns:
        str: The name of the expense.
    """
    while True:
        name_expense = input("Enter name of the expense: ")
        try:
            if name_expense == '' or len(name_expense) < 0:
                print("Try again, there is empty space")
            else:
                return name_expense
        except Exception:
            print(f"{Fore.RED}Try again, Error Value{Style.RESET_ALL}")


def get_ammount_expense() -> float:
    """
    Prompt the user to enter the amount of the expense.

    Returns:
        float: The amount of the expense.
    """
    while True:
        try:
            ammount_expense = float(input("Enter amount of the expense: $"))
            if ammount_expense < 0 or ammount_expense == '':
                print("Don't save with value 0 or something else")
            else:
                return ammount_expense
        except ValueError:
            print(f"{Fore.RED}Try again, Error Value{Style.RESET_ALL}")


def get_user_expense() -> Expense:
    """
    Gather user input to create a new Expense instance.

    Returns:
        Expense: The newly created expense object.
    """
    name_expense = get_name_expense()
    category_expense = [
        "🏠 Home",
        "🎥 Entertainent",
        "⚽ Funny",
        "💼 Work",
        "🚌 Transportation",
        "🍔 Food"
    ]
    ammount_expense = get_ammount_expense()

    while True:
        print("\nCategory: 🔽")
        for i, category in enumerate(category_expense):
            print(f"    {i + 1} {category}")

        len_category = len(category_expense)
        selected_range = f"[ 1 - {len_category} ] "

        selected_index = int(input(f"Enter number according to the range {selected_range}")) - 1
        if selected_index in range(len(category_expense)):
            new_expense = category_expense[selected_index]
            return Expense(
                name=name_expense,
                category=new_expense,
                ammount=ammount_expense,
            )
        else:
            print("Please, Try again")


def save_to_file(datas_user: Expense) -> bool:
    """
    Save the user's expense to 'data.json' file.

    If the file does not exist, it will be created. The new expense is appended to existing data.

    Args:
        datas_user (Expense): The expense to save.

    Returns:
        bool: True if data is saved successfully, False otherwise.
    """
    save_data = "data.json"

    if os.path.exists(save_data):
        with open(save_data, "r") as file:
            try:
                data_list = json.load(file)
            except Exception:
                data_list = []
    else:
        data_list = []

    new_entry = {
        "name": datas_user.name,
        "category": datas_user.category,
        "amount": datas_user.ammount,
    }

    data_list.append(new_entry)

    with open(save_data, "w") as file:
        json.dump(data_list, file)

    if os.path.exists(save_data):
        print(f"{Fore.GREEN}Successfully saved data{Style.RESET_ALL}")
        return True
    else:
        print(f"{Fore.RED}Failed to save data{Style.RESET_ALL}")
        return False


def main():
    """
    Main function to manage the application flow.

    Provides a menu to the user to add expenses, view totals, or exit.
    """
    while True:
        print("\nMenu:")
        print("1. Add an expense")
        print("2. Show totals by category")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                user_expense = get_user_expense()
                save_to_file(user_expense)
            elif choice == 2:
                calculate_totals()
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
