def main_menu():
    info = "Select one of the options: "
    print(info)

    choose_menu = [
        "Login",
        "Sign up",
        "Trip Search",
        "Book Trip",
        "My Trips",
    ]

    for i, menu in enumerate(choose_menu):
        print(f"{i + 1} {menu}")

    while True:
        try:

            pass
        except:
            pass
    pass

def main():
    print("Buy your tickets")
    main_menu()

if __name__ == "__main__":
    main()
