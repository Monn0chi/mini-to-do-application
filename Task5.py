contacts = {}

while True:
    print("\n--- Contact Book Manager ---")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact by name")
    print("4. Delete a contact")
    print("5. Exit")
    
    option = input("Choose an option: ")
    
    if not option.isdigit():
        print("Invalid input! Please enter a number between 1 and 5.")
        continue
    
    option = int(option)
    
    if option == 1:
        name = input("Enter contact name: ").strip()
        if not name:
            print("Name cannot be empty!")
        elif name in contacts:
            print(f"Contact '{name}' already exists with phone number: {contacts[name]}")
        else:
            phone = input("Enter phone number: ").strip()
            if phone:
                contacts[name] = phone
                print(f"Contact '{name}' added successfully!")
            else:
                print("Phone number cannot be empty!")
    
    elif option == 2:
        if not contacts:
            print("Your contact book is empty.")
        else:
            print("\n--- All Contacts ---")
            for name, phone in contacts.items():
                print(f"Name: {name}, Phone: {phone}")
    
    elif option == 3:
        if not contacts:
            print("Your contact book is empty.")
        else:
            search_name = input("Enter contact name to search: ").strip()
            
            if not search_name:
                print("Name cannot be empty!")
            elif search_name in contacts:
                print(f"\n Contact found!")
                print(f"Name: {search_name}, Phone: {contacts[search_name]}")
            else:
                print(f"Contact '{search_name}' not found in your contact book.")
    
    elif option == 4:
        if not contacts:
            print("Your contact book is empty. Nothing to delete.")
        else:
            print("\n--- All Contacts ---")
            for name, phone in contacts.items():
                print(f"Name: {name}, Phone: {phone}")
            
            delete_name = input("\nEnter contact name to delete: ").strip()
            
            if not delete_name:
                print("Name cannot be empty!")
            elif delete_name in contacts:
                confirm = input(f"Are you sure you want to delete '{delete_name}'? (yes/no): ").lower()
                if confirm == "yes":
                    deleted_phone = contacts[delete_name]
                    del contacts[delete_name]
                    print(f" Contact '{delete_name}' (Phone: {deleted_phone}) deleted successfully!")
                else:
                    print("Deletion cancelled.")
            else:
                print(f"Contact '{delete_name}' not found in your contact book.")
    
    elif option == 5:
        print("Exiting the Contact Book. Goodbye!")
        break
    
    else:
        print("Invalid option! Please choose a number between 1 and 5.")