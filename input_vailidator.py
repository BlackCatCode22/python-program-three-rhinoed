# Description: This file contains functions that validate user input
# File: input_validator.py
# Author: Mark Edmunds


# validate name input and formats it
def validate_name_input(input_string):
    """This function validates a name input"""
    if input_string != "":
        input_string = input_string.strip()
        input_string = input_string[0].upper() + input_string[1:].lower()
        return input_string
    else:
        return None


# validate search input
def validate_search_input(input_string):
    if input_string != "":
        input_string = input_string.strip()
        input_string = input_string.split(" ")
        modified_input_string = ""
        for word in input_string:
            word = word[0].upper() + word[1:].lower()
            modified_input_string += word + " "

        modified_input_string = modified_input_string.strip()
        return modified_input_string
    else:
        return None


# validate phone number input
def validate_phone_input(input_string):
    """This function validates a phone number input"""
    if input_string != "":
        input_string = input_string.strip()
        if input_string[0] == "(" and input_string[4] == ")" and input_string[8] == "-":
            input_string = input_string[1:4] + input_string[5:8] + input_string[9:]
            return input_string
        elif input_string[3] == "-" and input_string[7] == "-":
            return input_string
        elif len(input_string) == 7:
            input_string = input_string[:3] + "-" + input_string[3:]
            return input_string
        elif len(input_string) == 10:
            input_string = input_string[:3] + "-" + input_string[3:6] + "-" + input_string[6:]
            return input_string
        elif input_string.find(".") != -1 or input_string.find("x") != -1:
            index_of_x = input_string.find("x")
            input_string = input_string[0:index_of_x]
            input_string = input_string.strip()
            return input_string
        else:
            return None
    else:
        return None


def validate_email_input(input_string):
    """This function validates an email input"""
    if input_string != "":
        input_string = input_string.strip()
        if input_string.find("@") != -1 and input_string.find(".") != -1:
            return input_string
        else:
            return None
    else:
        return None
