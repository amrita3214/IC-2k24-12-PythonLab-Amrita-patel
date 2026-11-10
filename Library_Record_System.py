
books = {
    "B1": {
        "title": "Python Basics",
        "author": "Rao",
        "copies": 2,
        "issued_to": []
    },
    "B2": {
        "title": "Data Structures",
        "author": "Iyer",
        "copies": 1,
        "issued_to": []
    },
    "B3": {
        "title": "Algorithms",
        "author": "Rao",
        "copies": 1,
        "issued_to": []
    }
}

while True:
    print("\n1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        isbn = input("ISBN: ")

        if isbn in books:
            books[isbn]["copies"] += int(input("Additional copies: "))
        else:
            title = input("Title: ")
            author = input("Author: ")
            copies = int(input("Copies: "))

            books[isbn] = {
                "title": title,
                "author": author,
                "copies": copies,
                "issued_to": []
            }

        print("Book added!")

    elif choice == "2":
        isbn = input("Enter ISBN: ")
        member = input("Member ID: ")

        if isbn not in books:
            print("Book not found!")

        elif member in books[isbn]["issued_to"]:
            print("Member already holds this book!")

        else:
            held = [
                b for b in books.values()
                if member in b["issued_to"]
            ]

            if len(held) >= 2:
                print("Member already has 2 books!")

            elif books[isbn]["copies"] <= 0:
                print("No copies available!")

            else:
                books[isbn]["copies"] -= 1
                books[isbn]["issued_to"].append(member)
                print("Book issued successfully!")

    elif choice == "3":
        isbn = input("Enter ISBN: ")
        member = input("Member ID: ")

        if isbn in books and member in books[isbn]["issued_to"]:
            books[isbn]["issued_to"].remove(member)
            books[isbn]["copies"] += 1
            print("Book returned successfully!")
        else:
            print("Member does not hold this book!")

    elif choice == "4":
        isbn = input("Enter ISBN: ")
        print(books.get(isbn, "Book not found!"))

    elif choice == "5":

        author = input("Enter author name: ")

        result = {
            isbn: b["title"]
            for isbn, b in books.items()
            if b["author"].lower() == author.lower()
        }

        print("Books by author:", result)

        member_books = {}

        for isbn, b in books.items():
            for member in b["issued_to"]:
                member_books.setdefault(member, []).append(b["title"])

        multiple = {
            m: titles
            for m, titles in member_books.items()
            if len(titles) > 1
        }

        print("Members holding more than one book:", multiple)

        unavailable = [
            b["title"] for b in books.values()
            if b["copies"] == 0
        ]

        print("Unavailable books:", unavailable)

        never_issued = [
            b["title"] for b in books.values()
            if not b["issued_to"]
        ]

        print("Never issued:", never_issued)

    elif choice == "6":
        break

    else:
        print("Invalid choice!")
