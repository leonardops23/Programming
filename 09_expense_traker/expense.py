class Expense:
    def __init__(self, name, category, ammount):
        self.name = name
        self.category = category
        self.ammount = ammount

    def __repr__(self):
        return f"Expense: {self.name} - {self.category} - {self.ammount}"

def get_user_expense():
    # get name, category and ammount
    name_expense = input("Enter name of the expense: ")
    category_expense = [
        "🏠 Home",
        "🎥 Entertainent",
        "⚽ Funny",
        "💼 Work",
        "🚌 Trasnportation",
        "🍔 Food"
    ]
    ammount_expense = float(input("Enter ammount of the expense: "))

    while True:
        print("\nCategory: 🔽")
        for i, category in enumerate(category_expense):
            print(f"{i + 1} {category}")

        len_category = len(category_expense)
        selected_range = f"[ 1 - {len_category} ]"

        selected_index = int(input(f"Enter number according to the range {selected_range}"))
        if selected_index in range(len(category_expense)):
            new_expense = category_expense[selected_index]
            return Expense(
                name=name_expense,
                category=new_expense,
                ammount=ammount_expense,
            )
        else:
            print("Please, Try again")

def main():

    user_expense = get_user_expense()
    print(user_expense)

if __name__ == "__main__":
    main()
