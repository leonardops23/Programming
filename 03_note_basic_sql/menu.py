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
        elif choice == '3':
            select_id = int(input("ID of note to update: "))
            title = input("New title: ")
            content = input("New content: ")
            update_note(select_id, title, content)
        elif choice == '4':
            id_note = int(input("Id of the note to dalelte: "))
            delete_note(id_note)
            print("Note deleted successfully!")
        elif choice == '5':
            break


def menu():
    print('1- Add new Note')
    print('2- See all Notes')
    print('3- Update Note')
    print('1- Delete Note')
