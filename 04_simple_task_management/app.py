
def select_option() -> int:
    options = [
        'Register',
        'Login',
        'Exit',
    ]

    len_option = len(options)
    print(len_option)

    for i, option in enumerate(options):
        print(f"{i + 1} {option}")

    while True:
        choice = input("Choose an option [1 - 3]: ")
        if choice.isdigit():
            int_choice = int(choice)
            if int_choice in range(1, len_option + 1):
                return int_choice
            else:
                print(f"Must be an range of [1 - {len_option}]")
        else:
            print("Enter a number")


def main():
    choice = select_option()

    if choice == 1:
        pass

if __name__ == "__main__":
    main()
