while True:
    print("\n1.Add  2.Display  3.Search  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Enter name: ")
        marks = input("Enter marks: ")

        with open("students.txt", "a") as f:
            f.write(name + "," + marks + "\n")

        print("Record added")

    elif ch == 2:
        with open("students.txt", "r") as f:
            print(f.read())

    elif ch == 3:
        name = input("Enter name to search: ")
        found = False

        with open("students.txt", "r") as f:
            for line in f:
                if line.startswith(name + ","):
                    print(line)
                    found = True

        if not found:
            print("Student not found")

    elif ch == 4:
        break