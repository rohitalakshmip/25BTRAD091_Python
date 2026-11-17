class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)


name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

b = BankAccount(name, balance)

while True:
    print("\n1.Deposit")
    print("2.Withdraw")
    print("3.Balance Enquiry")
    print("4.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        amount = float(input("Enter deposit amount: "))
        b.deposit(amount)

    elif ch == 2:
        amount = float(input("Enter withdrawal amount: "))
        b.withdraw(amount)

    elif ch == 3:
        b.display()

    elif ch == 4:
        print("Thank you")
        break

    else:
        print("Invalid choice")