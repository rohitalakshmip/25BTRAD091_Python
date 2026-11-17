
students = []

def add_student():
    name = input("Enter student name: ")

    students.append({
        "name": name,
        "attendance": []
    })

    print("Student added successfully")

def update_attendance():
    name = input("Enter student name: ")

    for student in students:
        if student["name"] == name:
            status = input("Enter attendance (P/A): ").upper()

            if status == "P" or status == "A":
                student["attendance"].append(status)
                print("Attendance updated")
            else:
                print("Invalid status")
            return

    print("Student not found")

def display_attendance():
    for student in students:
        print(student["name"], student["attendance"])

def calculate_percentage():
    threshold = float(input("Enter attendance threshold: "))

    for student in students:
        total = len(student["attendance"])
        present = student["attendance"].count("P")

        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0

        print(student["name"], ":", percentage, "%")

        if percentage < threshold:
            print("Below attendance threshold")
        else:
            print("Attendance sufficient")

while True:
    print("\n1.Add Student")
    print("2.Update Attendance")
    print("3.Display Attendance")
    print("4.Calculate Percentage")
    print("5.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        add_student()

    elif ch == 2:
        update_attendance()

    elif ch == 3:
        display_attendance()

    elif ch == 4:
        calculate_percentage()

    elif ch == 5:
        print("Thank you")
        break

    else:
        print("Invalid choice")
