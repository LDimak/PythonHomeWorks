#
# file = []
# def open_phone_book():
#     with open('phone_book.txt' ,'r', encoding='utf-8') as data:
#         file = data.readlines()
#         for i in file:
#             print(' '.join(i.split(';')))
# def save_phone_book():
#     pass
# def show_phone_book():
#     if len(file) == 0:
#         print('Ваш справочник контактов пуст')
#     else:
#         for i in file:
#             print(' '.join(i.split(';')))
# def add_contact():
#     user_info = input('Введите данные нового контакта: ')
#     user_info.split(' '.join(';'))
#     file.append(user_info)
#
# def change_contact():
#     pass
# def search_contact():
#     pass
# def delete_contact():
#     pass
#
# open_phone_book()
#
# add_contact()
# open_phone_book()
# Define the phone book file path

import os

# File path
file_path = os.path.join(os.getcwd(), "contacts.txt")

# Open file
def open_file():
    with open(file_path, "r") as f:
        contacts = f.readlines()
        for contact in contacts:
            print(contact)

# Save file
def save_file():
    with open(file_path, "a") as f:
        name = input("Enter the name of the contact you want to add: ")
        phone = input("Enter the phone number of the contact you want to add: ")
        f.write(f"{name}, {phone}\n")
        print("Contact added successfully!")

# Show contacts
def show_contacts():
    with open(file_path, "r") as f:
        contacts = f.readlines()
        for contact in contacts:
            print(contact)

# Add contact
def add_contact():
    save_file()

# Update contact
def update_contact():
    with open(file_path, "r") as f:
        lines = f.readlines()
    name = input("Enter the name of the contact you want to update: ")
    phone = input("Enter the new phone number of the contact: ")
    for i, line in enumerate(lines):
        if name in line:
            lines[i] = f"{name}, {phone}\n"
            break
    with open(file_path, "w") as f:
        f.writelines(lines)
    print("Contact updated successfully!")

# Find contact
def find_contact():
    search_key = input("Enter the name of the contact you want to find: ")
    with open(file_path, "r") as f:
        contacts = f.readlines()
        for contact in contacts:
            if search_key in contact:
                print(contact)

# Delete contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    with open(file_path, "r") as f:
        lines = f.readlines()
    with open(file_path, "w") as f:
        for line in lines:
            if name not in line:
                f.write(line)
    print("Contact deleted successfully!")

# Exit program
def exit_program():
    print("Goodbye!")
    exit()