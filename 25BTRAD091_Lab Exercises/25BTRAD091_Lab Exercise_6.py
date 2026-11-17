num=int(input("Enter a positive integer: "))

# 1. PRIME NUMBER
if num<=1:
    prime_result="Not a prime number"
else:
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        prime_result="prime number"
    else:
        prime_result="Not a prime number"


# 2. FACTORIAL
if num<0:
    fact_result = "Factorial does not exist for negative numbers" 
elif num==0:
    fact_result = 1
else:
    fact_result = 1
    for i in range(1,num+1):
        fact_result*=i

print(f"\n--------RESULTS For {num}--------\n")
print(f"Prime Check: {prime_result}")
print(f"Factorial: {fact_result}")