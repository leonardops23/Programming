class Expense:
    def __init__(self, name, category, ammount):
        self.name = name
        self.category = category
        self.ammount = ammount


def get_user_expense():
    # get name, category and ammount
    name_expense = input("Enter name of the expense: ")
    category_expense = {
        "🏠 Home",
        "🎥 Entertainent",
        "⚽ Funny",
        "💼 Work",
        "🚌 Trasnportation",
        "🍔 Food"
    }
    ammount_expense = int(input("Enter ammount of the expense: "))

    print("Category🚀: ")
    while True:
        print(category_expense)
        break

def main():
    get_user_expense()

if __name__ == "__main__":
    main()
