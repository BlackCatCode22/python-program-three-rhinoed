# Readme for Program 3
### by Mark Edmunds

## Overview
This program grew in scale as I worked on it. After implementing the basic requirements of creating a list of dictionaries, a view function, and a search function. I added more features. 
My process for this program like most of my projects I worked and completed coding sections until running into issues and then consulting resources on the web and in this class.

The options for the user are:
- Add contact
- View contacts
- Search contacts
- Update contact
- Delete contact

`add_contact`
```python
def add_contact():
    """This function adds a contact to the contacts list"""
    # Create a dictionary for the contact
    contact = create_contact()
    if contact is not None:
        contacts.append(contact)

    # Write the contacts to the file
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=4)

```
`view_contacts`
```python
def view_contacts():
    """This function displays all contacts in the contacts list"""
    print("Your contacts are: \n")

    # Print all the contacts
    for i in range(len(contacts) - 1):
        display_contact(i)
```
`search_contacts`
```python
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
```
`update_contact`
```python

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
```
`delete_contact`
```python
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
```
Also, the changes are persistent. The program will save the changes to the file and load them when the program is run again.
I accomplished by using the built-in open() function, I was able to read and write the data to a file. 
The data is in json format and when loaded is converted to a list of contact dictionaries. 

##### Use of modules
Because the main program was growing in size. I split some of the presentation and validation code into separate file and imported them.
These include:

- contact_manager_menu.py
- input_validation.py

There is also a third party module which I used

- colorama

This is used to add color o the output.

#### Testing
Prior to the implementation of loading data from a file. I hard coded a list with some contacts.
After that I used the program and noted any errors or bugs. And fixed them. I know such manual testing is unlikely to catch all errors. 
But I did my best to test the program and fix any errors I found. I did try my hand at a more programmatic approach to testing.
I did this by using pytest to test some of the input validation functions.  And it helped me identify some cases I had not considered.

#### Conclusion
In the end I'm happy with the program.However, there are numerous things which could be improved and I may continue to work on this if time allows.
