# Contact Book Management System

## Features and Functionality

This Python script implements a simple Contact Book Management System using a dictionary to store contact information. The program provides various operations such as adding, searching, viewing, updating, and deleting contacts.

### Contact Book Dictionary

- The script initializes an empty dictionary named `contact_book` to store contacts.

### Contact Book Menu

- The script enters a `while` loop to display a menu for contact book operations.

- The menu includes the following options:
  1. **Add Contact:** Allows the user to add a new contact with a name and phone number.
  2. **Search Contact:** Searches for a contact by name and displays the associated phone number if found.
  3. **View Contacts:** Displays all contacts in the contact book.
  4. **Update Contact:** Updates the phone number of an existing contact.
  5. **Delete Contact:** Deletes an existing contact from the contact book.
  6. **Exit:** Exits the contact book application.

### Contact Operations

1. **Add Contact (Option 1):**
   - The user is prompted to enter a name and phone number.
   - The contact is added to the `contact_book` dictionary.

2. **Search Contact (Option 2):**
   - The user inputs a contact name.
   - If the contact is found, the associated phone number is displayed.
   - If not found, a message is shown.

3. **View Contacts (Option 3):**
   - Displays all contacts in a tabular format.

4. **Update Contact (Option 4):**
   - The user inputs the name of the contact to be updated.
   - If the contact is found, the user can update the phone number.
   - Displays the updated contact list.

5. **Delete Contact (Option 5):**
   - The user inputs the name of the contact to be deleted.
   - Confirms the deletion with a prompt.
   - Displays the updated contact list after deletion.

6. **Exit (Option 6):**
   - Exits the program using `sys.exit(0)`.

### Running the Contact Book

- To use the contact book, execute the script.
- Follow the on-screen menu to perform various contact book operations.

### Sample Usage

```python
while True:
    print("\nWelcome to your Contact Book")
    # ... (menu options)
    ch = int(input("Enter your choice:"))
    # ... (perform contact book operations based on user choice)
    if ch == 6:
        sys.exit(0)
