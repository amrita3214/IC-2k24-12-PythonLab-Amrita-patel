students = {
    101: {"name": "Asha", "marks": {"Math": 88, "Physics": 76, "Chem": 92}},
    102: {"name": "Ravi", "marks": {"Math": 35, "Physics": 58, "Chem": 64}},
    103: {"name": "Meena", "marks": {"Math": 72, "Physics": 81, "Chem": 69}}
}

while True:
    print("\n1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Show Student")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = int(input("Enter roll number: "))

        if roll in students:
            print("Duplicate roll number!")
        else:
            name = input("Enter name: ")
            marks = {}

            n = int(input("Enter number of subjects: "))

            for i in range(n):
                sub = input("Subject: ")
                score = int(input("Marks: "))

                if 0 <= score <= 100:
                    marks[sub] = score
                else:
                    print("Invalid marks!")

            students[roll] = {"name": name, "marks": marks}
            print("Student added successfully!")

    elif choice == "2":
        roll = int(input("Enter roll number: "))

        if roll in students:
            sub = input("Enter subject: ")
            score = int(input("Enter marks: "))

            if 0 <= score <= 100:
                students[roll]["marks"][sub] = score
                print("Marks updated!")
            else:
                print("Marks must be between 0 and 100.")
        else:
            print("Student not found!")

    elif choice == "3":
        roll = int(input("Enter roll number: "))

        if roll in students:
            del students[roll]
            print("Student deleted!")
        else:
            print("Student not found!")

    elif choice == "4":
        roll = int(input("Enter roll number: "))

        if roll in students:
            print(students[roll])
        else:
            print("Student not found!")

    elif choice == "5":
        averages = {
            r: round(sum(s["marks"].values()) / len(s["marks"]), 2)
            for r, s in students.items() if s["marks"]
        }

        print("Averages:", averages)

        if averages:
            topper = max(averages, key=averages.get)
            print("Topper:", students[topper]["name"])

        subjects = set(
            sub for s in students.values()
            for sub in s["marks"]
        )

        for sub in subjects:
            scores = [
                (s["name"], s["marks"][sub])
                for s in students.values() if sub in s["marks"]
            ]
            if scores:
                print("Highest in", sub, ":", max(scores, key=lambda x: x[1]))

        for s in students.values():
            failed = [sub for sub, m in s["marks"].items() if m < 40]
            if failed:
                print("Below 40:", s["name"], failed)

        grades = {"A": [], "B": [], "C": [], "D": [], "F": []}

        for r, avg in averages.items():
            grade = (
                "A" if avg >= 90 else
                "B" if avg >= 75 else
                "C" if avg >= 60 else
                "D" if avg >= 40 else "F"
            )
            grades[grade].append(students[r]["name"])

        print("Grade-wise grouping:", grades)

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid choice!")
