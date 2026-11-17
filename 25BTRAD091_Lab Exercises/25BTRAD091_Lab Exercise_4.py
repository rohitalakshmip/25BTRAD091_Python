import math

def simple_calculator():
    print("\n--- PART 1: SIMPLE CALCULATOR ---")
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ").strip()
    num2 = float(input("Enter second number: "))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        result = "Invalid operator"

    print(f"Result: {result}")


def area_calculator():
    print("\n--- PART 2: AREA CALCULATIONS ---")
    print("1. Area of Circle")
    print("2. Area of Rectangle")
    print("3. Area of Triangle")
    
    choice = input("Select a shape (1-3): ").strip()

    if choice == '1':
        radius = float(input("Enter radius of circle: "))
        area = math.pi * (radius ** 2)
        print(f"Area of Circle: {area:.2f}")

    elif choice == '2':
        length = float(input("Enter length of rectangle: "))
        width = float(input("Enter width of rectangle: "))
        area = length * width
        print(f"Area of Rectangle: {area:.2f}")

    elif choice == '3':
        base = float(input("Enter base of triangle: "))
        height = float(input("Enter height of triangle: "))
        area = 0.5 * base * height
        print(f"Area of Triangle: {area:.2f}")

    else:
        print("Invalid choice!")


# Main Program Execution
def main():
    print("      LAB EXERCISE 4: MAIN MENU         ")
    print("1. Run Simple Calculator")
    print("2. Run Area Calculator")
    print("3. Run Both Sequentially")
    
    option = input("Enter your option (1-3): ").strip()

    if option == '1':
        simple_calculator()
    elif option == '2':
        area_calculator()
    elif option == '3':
        simple_calculator()
        area_calculator()
    else:
        print("Invalid choice! Exiting program.")

if __name__ == "__main__":
    main()