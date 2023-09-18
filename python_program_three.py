#!/usr/local/bin/python3
# ******************************************* Header *****************************************************
# Program: Python Program Three
# Class: CIT 95 Fall 2023
# Programmer: Mark Edmunds
# File Name: python_program_three.py
# Date: 9/12/2023
# ******************************************** Imports ***************************************************
import json
import contact_manager_menu as menu
import input_vailidator as check
from colorama import Fore, Back, Style


# ******************************************** Functions *************************************************


# read contacts from file
def read_json_file(file_name):
    """This function reads a json file and returns an array of contacts"""
    array_from_file = []
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
        for d in data:
            first_name = d["first_name"]
            last_name = d["last_name"]
            full_name = d["first_name"] + " " + d["last_name"]
            phone_number = d["phone_number"]
            email_address = d["email_address"]
            contact = {"first_name": first_name,
                       "last_name": last_name,
                       "full_name": full_name,
                       "phone_number": phone_number,
                       "email_address": email_address
                       }
            array_from_file.append(contact)
    return array_from_file


# add a contact
def add_contact():
    """This function adds a contact to the contacts list"""
    # Create a dictionary for the contact
    contact = create_contact()
    if contact is not None:
        contacts.append(contact)

    # Write the contacts to the file
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=4)


# create a contact from user input
def create_contact():
    """This function creates a contact from user input"""
    exit_without_creating = False
    # Prompt user for contact information
    first_name = check.validate_name_input(input("Enter first name: "))
    last_name = check.validate_name_input(input("Enter last name: "))
    while first_name is None or last_name is None:
        print("Invalid input please try again")
        first_name = check.validate_name_input(input("Enter first name: "))
        last_name = check.validate_name_input(input("Enter last name: "))
    if check_for_name(first_name, last_name):
        return None
    phone_number = check.validate_phone_input(input("Enter phone number: "))
    email_address = check.validate_email_input(input("Enter email address: "))
    while phone_number is None or email_address is None:
        print("Invalid input please try again")
        phone_number = check.validate_phone_input(input("Enter phone number: "))
        email_address = check.validate_email_input(input("Enter email address: "))
    phone_is_unique = search_contact(phone_number)
    email_is_unique = search_contact(email_address)
    # Create a dictionary for the contact
    if phone_is_unique != -1:
        print("A contact with that phone number already exists")
        return None
    if email_is_unique != -1:
        print("A contact with that email address already exists")
        return None
    else:
        contact = {'first_name': first_name,
                   'last_name': last_name,
                   "full_name": first_name + " " + last_name,
                   'phone_number': phone_number,
                   'email_address': email_address}
        return contact


# check if contact name is unique
def check_for_name(first_name, last_name):
    """This function checks if a name is in the contacts list"""
    i = 0
    # Check if the contact name is unique if not, ask if user wants to update the contact
    for c in contacts:
        name = c["first_name"] + " " + c["last_name"]
        if first_name + " " + last_name == name:
            selection = input("A contact with that name already exists would you like to update it? (y/n): ")
            if selection == "y":
                keys = input(
                    "What would you like to update? phone_number (enter 1),email_address (enter 2) or 3 for both) : ")
                update_contact(i, keys)
            return True

    i += 1


# view all contacts
def view_contacts():
    """This function displays all contacts in the contacts list"""
    print("Your contacts are: \n")

    # Print all the contacts
    for i in range(len(contacts) - 1):
        display_contact(i)


# display a contact
def display_contact(index):
    """This function displays a contact"""
    # output contact information
    contact = contacts[index]
    print(Back.LIGHTGREEN_EX, Fore.BLACK, Style.BRIGHT + "Contact " + str(index + 1), end=" ")
    print(Style.RESET_ALL)
    for key in contact.keys():
        displayed_key = key.replace("_", " ")
        if key == "full_name":
            continue
        print(displayed_key + ": " + contact[key])
    print(" ")


# search for a contact
def search_contact(search=None):
    """This function searches for a contact
    :type search: str
    """
    i = 0
    # Prompt user for search criteria
    if search is None:
        search_for = check.validate_search_input(input("Enter search criteria: "))
        while search_for is None:
            print("Invalid input please try again")
            search_for = check.validate_search_input(input("Enter search criteria: "))
    else:
        search_for = search
    # iterate through contacts searching for search criteria
    for c in contacts:
        search_set = set(c.values())
        # if search criteria is found display contact
        if search_for in search_set:
            display_contact(i)
            menu.status_message = "Contact found"
            return i
        else:
            menu.status_message = "No results found"
            i += 1
    return -1


# update a contact
def update_contact(index, user_selection):
    """This function updates a contact"""
    if user_selection == "1":
        keys = ["phone_number"]
    elif user_selection == "2":
        keys = ["email_address"]
    elif user_selection == "3":
        keys = ["phone_number", "email_address"]
    else:
        print("Invalid input please try again")
        return
    for key in keys:
        contacts[index][key] = input(f"Enter new {key}: ")
    # save contacts to file
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=4)


# delete a contact
def delete_contact(contact_number):
    """This function deletes a contact"""
    # confirm delete
    delete_prompt = input("Are you sure you want to delete this contact this action cannot be undone? (y/n): ")
    if delete_prompt == "y":
        try:
            valid_int = int(contact_number)
            contacts.pop(int(valid_int) - 1)
        except ValueError:
            print("Invalid input must be a number")
            delete_contact(input("Enter the contact number: "))
        with open("contacts.json", "w") as file:
            json.dump(contacts, file, ensure_ascii=False, indent=4)
    else:
        print("Contact not deleted")


# ******************************************** Main Program *************************************************
# main program
while True:
    # list of contacts
    contacts = sorted(read_json_file("contacts.json"), key=lambda i: i['last_name'])
    # print menu options for user to choose from
    print(Fore.LIGHTGREEN_EX + menu.draw_menu())
    print(Style.RESET_ALL)
    # get user menu selection
    user_input = input("Enter a number or type exit to quit: ")
    # check user input
    if user_input == "1":
        add_contact()
    elif user_input == "2":
        view_contacts()
    elif user_input == "3":
        results = search_contact()
        if results == -1:
            print("No results found")
    elif user_input == "4":
        print("You can update a contact by searching for it")
        user_search = search_contact()
        if user_search is not None:
            user_keys = input(
                "What would you like to update? phone_number (enter 1),email_address (enter 2) or 3 for both) : ")
            update_contact(user_search, user_keys)
    elif user_input == "5":
        print("You can delete a contact by enter the contact number which can be found by searching for a contact")
        continue_prompt = input("do you want to continue? (y/n): ")
        if continue_prompt == "y":
            delete_contact(input("Enter the contact number: "))
    elif user_input == "exit":
        # exit program
        print("exiting program")
        break
    else:
        print("Invalid input please try again")
