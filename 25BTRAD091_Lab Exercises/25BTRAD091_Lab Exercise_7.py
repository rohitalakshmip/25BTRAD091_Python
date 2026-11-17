def fibonacci(n):
    if n <= 0:
        return 0 
    elif n ==1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter the number of terms : "))
if terms <= 0:
    print("please enter a positive integer greater than 0:")
else:
    print(f"Fibonacci sequence up to {terms} terms:")
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()
    

