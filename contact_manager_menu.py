# Description: This file contains the menu for the contact manager
# written for python_program_three.py
# File: contact_manager_menu.py
# Author: Mark Edmunds
# Date: 9/12/2023




status_message = ""
ver = "0.0.1"
# option for the menu
menu_items = [
    "1 = Add contact",
    "2 = View All contacts",
    "3 = Search for contact",
    "4 = Update contact",
    "5 = Delete contact",
]

# display the menu
def draw_menu(message=""):
    global ver
    global menu_items
    menu = (
            "**********************************************************************************************\n"
            f"*                        Welcome to Python Contacts Manager {ver}                            *\n"
            "**********************************************************************************************\n"
            "                       Please select an option from the menu below                            \n"
            " Menu:                                                                                       \n"
            " " + "\n ".join(menu_items) +
            ""
            " " + message +
            " "
    )
    return menu
