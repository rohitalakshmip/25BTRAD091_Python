class Book:
    def __init__(self, name):
        self.name = name
        self.available = True


class Library:
    def __init__(self):
        self.books = [
            Book("Python"),
            Book("Java"),
            Book("C")
        ]

    def display(self):
        for book in self.books:
            if book.available:
                print(book.name, "- Available")
            else:
                print(book.name, "- Issued")

    def issue(self, name):
        for book in self.books:
            if book.name == name and book.available:
                book.available = False
                print("Book issued successfully")
                return

        print("Book not available")

    def return_book(self, name):
        for book in self.books:
            if book.name == name and not book.available:
                book.available = True
                print("Book returned successfully")
                return

        print("Invalid return")


l = Library()

while True:
    print("\n1.Display Books")
    print("2.Issue Book")
    print("3.Return Book")
    print("4.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        l.display()

    elif ch == 2:
        name = input("Enter book name: ")
        l.issue(name)

    elif ch == 3:
        name = input("Enter book name: ")
        l.return_book(name)

    elif ch == 4:
        break

    else:
        print("Invalid choice")