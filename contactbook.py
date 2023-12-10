import sys
#dictionary to store the contacts
contact_book = {}
#displaying all contacts
def contacts():
    print("Name\t\tPhone Number")
    for key in contact_book:
        print("{}\t\t{}".format(key,contact_book.get(key)))
#Contact Book Menu
while True:
    print("\nWelcome to your Contact Book")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        Name = input("Enter name:")
        Phone = int(input("Enter phone number:"))
        contact_book[Name] = Phone
    elif ch == 2:
        search_name = input("Enter contact name:")
        if search_name in contact_book:
            print("Contact Found")
            print(search_name, "'s Phone Number is:",contact_book[search_name])
        else:
            print("The entered name is not found in the Contact Book!!")
    elif ch == 3:
        if not contact_book:
            print("The Contact Book is EMPTY!!!")
        else:
            print()
            contacts()
    elif ch == 4:
        update_contact = input("Enter the contact to be updated:")
        if update_contact in contact_book:
            Phone = int(input("Enter Phone number:"))
            contact_book[update_contact] = Phone
            print("Contact Succesfully Updated!!!")
            print()
            contacts()
        else:
            print("Name not found in contacts!!")
    elif ch == 5:
        delete_contact = input("Enter contact to be deleted:")
        if delete_contact in contact_book:
            alert = input("Do you want to delete the contact? (y/n)").lower()
            if alert == 'y':
                contact_book.pop(delete_contact)
            print()
            contacts()
        else:
            print("Name not found in Contacts!!")
    elif ch == 6:
        sys.exit(0)
