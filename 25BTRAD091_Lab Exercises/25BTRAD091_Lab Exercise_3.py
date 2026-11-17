# Input
print("Enter two numbers ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmetic operators
Addition = num1 + num2
Subtraction = num1 - num2
Multiplication = num1 * num2
Division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

# output
print(f"Addition ({num1} + {num2}): {Addition}")
print(f"Subtraction ({num1} - {num2}): {Subtraction}")
print(f"Multiplication ({num1} * {num2}): {Multiplication}")
print(f"Division ({num1} / {num2}): {Division}")