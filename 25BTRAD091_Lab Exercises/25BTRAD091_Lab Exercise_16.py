import random

while True:
    n = int(input("Enter number of dice: "))

    for i in range(n):
        num = random.randint(1, 6)
        print("Dice", i + 1, ":", num)

    choice = input("Roll again? (yes/no): ")

    if choice == "no":
        print("Game Over")
        break