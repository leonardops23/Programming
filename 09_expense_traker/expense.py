from colorama import Fore
from colorama import Style
import json
import os

class Expense:
    def __init__(self, name, category, ammount):
        self.name = name
        self.category = category
        self.ammount = ammount

    def __repr__(self):
        return f"Expense: {self.name} - {self.category} - {self.ammount}"


def get_name_expense() -> str:
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
    while True:
        try:
            ammount_expense = float(input("Enter ammount of the expense: $"))
            if ammount_expense < 0 or ammount_expense == '':
                print("Don't save with value 0 or somenthing else")
            else:
                return ammount_expense
        except ValueError:
            print(f"{Fore.RED}Try again, Error Value{Style.RESET_ALL}")



def get_user_expense():
    # get name, category and ammount
    name_expense = get_name_expense()
    category_expense = [
        "🏠 Home",
        "🎥 Entertainent",
        "⚽ Funny",
        "💼 Work",
        "🚌 Trasnportation",
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
    save_data = "data.json"

    if os.path.exists(save_data):
        with open(save_data, "r") as file:
            try:
                data_list = json.load(file)
            except:
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
    user_expense = get_user_expense()
    # file save to json format
    save_to_file(user_expense)

if __name__ == "__main__":
    main()
