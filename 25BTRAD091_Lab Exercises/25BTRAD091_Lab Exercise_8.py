contacts = []

while True:
    print("\n1.Add  2.Search  3.Update  4.Delete  5.Display  6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts.append({"name": name, "phone": phone})

    elif ch == 2:
        name = input("Enter name: ")
        for c in contacts:
            if c["name"] == name:
                print(c)
                break
        else:
            print("Contact not found")

    elif ch == 3:
        name = input("Enter name: ")
        for c in contacts:
            if c["name"] == name:
                c["phone"] = input("New phone: ")
                print("Updated")
                break
        else:
            print("Contact not found")

    elif ch == 4:
        name = input("Enter name: ")
        for c in contacts:
            if c["name"] == name:
                contacts.remove(c)
                print("Deleted")
                break
        else:
            print("Contact not found")

    elif ch == 5:
        print(contacts)

    elif ch == 6:
        break