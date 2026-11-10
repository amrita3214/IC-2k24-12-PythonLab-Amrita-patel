
contacts = {
    "Aniket": {
        "phones": ["9876543245"],
        "email": "aniket@mail.com",
        "city": "Pune"
    },
    "Manoj": {
        "phones": ["9123456780", "9988776655"],
        "email": "manoj@mail.com",
        "city": "Delhi"
    },
    "Mira": {
        "phones": ["9203811111"],
        "email": "Mira@mail.com",
        "city": "Pune"
    }
}

while True:
    print("\n1. Add Contact")
    print("2. Add Another Number")
    print("3. Update Email or City")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Reports")
    print("7. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")

        if name in contacts:
            print("Contact already exists!")

        elif len(phone) != 10 or not phone.isdigit():
            print("Invalid phone number!")

        else:
            email = input("Enter email: ")
            city = input("Enter city: ")

            # Check duplicate phone number
            duplicate = False

            for c in contacts.values():
                if phone in c["phones"]:
                    duplicate = True

            if duplicate:
                print("Phone number already exists!")
            else:
                contacts[name] = {
                    "phones": [phone],
                    "email": email,
                    "city": city
                }
                print("Contact added successfully!")

    elif ch == "2":
        name = input("Enter name: ")
        phone = input("Enter new number: ")

        if name not in contacts:
            print("Contact not found!")

        elif len(phone) != 10 or not phone.isdigit():
            print("Invalid phone number!")

        else:
            duplicate = False

            for c in contacts.values():
                if phone in c["phones"]:
                    duplicate = True

            if duplicate:
                print("Number already belongs to another contact!")
            else:
                contacts[name]["phones"].append(phone)
                print("Number added successfully!")

    elif ch == "3":
        name = input("Enter name: ")

        if name in contacts:
            print("1. Update Email")
            print("2. Update City")

            option = input("Choose option: ")

            if option == "1":
                contacts[name]["email"] = input("New email: ")
                print("Email updated!")

            elif option == "2":
                contacts[name]["city"] = input("New city: ")
                print("City updated!")

            else:
                print("Invalid option!")

        else:
            print("Contact not found!")

    elif ch == "4":
        name = input("Enter name: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found!")

    elif ch == "5":
        search = input("Enter name or phone: ").lower()

        found = False

        for name, c in contacts.items():
            if search in name.lower() or search in c["phones"]:
                print(name, c)
                found = True

        if not found:
            print("Contact not found!")

    elif ch == "6":

        # Reverse lookup using comprehension
        reverse = {
            phone: name
            for name, c in contacts.items()
            for phone in c["phones"]
        }

        print("Reverse Lookup:", reverse)

        # Group contacts by city
        cities = {}

        for name, c in contacts.items():
            city = c["city"]

            if city not in cities:
                cities[city] = []

            cities[city].append(name)

        print("Contacts by City:", cities)

        # Contacts with multiple numbers
        multiple = []

        for name, c in contacts.items():
            if len(c["phones"]) > 1:
                multiple.append(name)

        print("Multiple Numbers:", multiple)

        # Display directory alphabetically
        print("Complete Directory:")

        for name in sorted(contacts):
            print(name, contacts[name])

    elif ch == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
