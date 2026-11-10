
employees = {
    "E1": {"name": "Kisan", "dept": "IT", "salary": 60000},
    "E2": {"name": "Mira", "dept": "HR", "salary": 45000},
    "E3": {"name": "Devi", "dept": "IT", "salary": 75000},
    "E4": {"name": "Naira", "dept": "Finance", "salary": 52000},
    "E5": {"name": "Om", "dept": "HR", "salary": 48000}
}

while True:
    print("\n1. Add Employee")
    print("2. Update Salary")
    print("3. Delete Employee")
    print("4. Search Employee")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        eid = input("Employee ID: ")

        if eid in employees:
            print("Employee already exists!")
        else:
            name = input("Name: ")
            dept = input("Department: ")
            salary = float(input("Salary: "))

            employees[eid] = {
                "name": name,
                "dept": dept,
                "salary": salary
            }
            print("Employee added!")

    elif choice == "2":
        eid = input("Enter employee ID: ")

        if eid in employees:
            salary = float(input("New salary: "))
            employees[eid]["salary"] = salary
            print("Salary updated!")
        else:
            print("Employee not found!")

    elif choice == "3":
        eid = input("Enter employee ID: ")

        if eid in employees:
            del employees[eid]
            print("Employee deleted!")
        else:
            print("Employee not found!")

    elif choice == "4":
        eid = input("Enter employee ID: ")
        print(employees.get(eid, "Employee not found"))

    elif choice == "5":

        payroll = {}
        headcount = {}

        for emp in employees.values():
            dept = emp["dept"]

            payroll[dept] = payroll.get(dept, 0) + emp["salary"]
            headcount[dept] = headcount.get(dept, 0) + 1

        print("Payroll:", payroll)
        print("Headcount:", headcount)

        highest = {}

        for emp in employees.values():
            dept = emp["dept"]

            if dept not in highest or emp["salary"] > highest[dept]["salary"]:
                highest[dept] = emp

        print("Highest paid employees:")

        for dept, emp in highest.items():
            print(dept, ":", emp["name"])

        sorted_emp = sorted(
            employees.items(),
            key=lambda x: x[1]["salary"],
            reverse=True
        )

        print("Salary order:")
        for eid, emp in sorted_emp:
            print(emp["name"], emp["salary"])

        # A new dictionary is created to protect original salaries.
        raised = {
            eid: {
                **emp,
                "salary": emp["salary"] * 1.10
            }
            for eid, emp in employees.items()
            if emp["salary"] < 50000
        }

        print("After 10% raise:", raised)

        avg_salary = {
            dept: payroll[dept] / headcount[dept]
            for dept in payroll
        }

        print("Department averages:", avg_salary)

        if avg_salary:
            best = max(avg_salary, key=avg_salary.get)
            print("Highest average salary:", best)

    elif choice == "6":
        break

    else:
        print("Invalid choice!")
