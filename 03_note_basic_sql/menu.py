from note_manager import *


def hanble_menu():
    # Handle options
    while True:
        menu()
        choice = input("Select the options: ")
        if choice == '1':
            title = input('Enter title: ')
            content = input('Enter the content: ')
            add_note(title, content)
            print("Note add succefully")
        elif choice == '2':
            notes = view_note()
            for note in notes:
                print(f"ID: {note[0]}, TITLE: {note[1]}, DATE: {note[3]}")
                print(f"Content: {note[2]}")
                print("-" * 30)
    
def menu():
    print('1- Add new Note')
    print('2- See all Notes')
    print('1- Update Note')
    print('1- Delete Note')

