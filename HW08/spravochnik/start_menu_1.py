from config_1 import *

# Main menu options
menu = {
    '1': open_file,
    '2': save_file,
    '3': show_contacts,
    '4': add_contact,
    '5': update_contact,
    '6': find_contact,
    '7': delete_contact,
    '8': exit_program
}


def main():
    while True:
        print('--- Phonebook Menu ---')
        print('1. Open file')
        print('2. Save file')
        print('3. Show contacts')
        print('4. Add contact')
        print('5. Modify contact')
        print('6. Search contact')
        print('7. Delete contact')
        print('8. Exit')

        choice = input('Enter your choice: ')

        if choice in menu:
            menu[choice]()
        else:
            print('Invalid choice. Please try again.\n')


if __name__ == '__main__':
    main()