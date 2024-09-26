
def create_note():
    print("Enter text: ")
    text = input()
    

def show_note():
    pass


def modify_note():
    pass


def delete_note():
    pass


def main():
    print("\n------- 🐍Welcome to note📓 ---------\n")
    options = [
        '🚀 Create Note',
        '🔎 Show Note',
        '📝 Modified Note',
        '🗑️ Delete Note'
    ]

    for index, option in enumerate(options):
        print("{} {}".format(index, option))

    number_select = input("\nSelect one👽: ")

    note = create_note()


main()

