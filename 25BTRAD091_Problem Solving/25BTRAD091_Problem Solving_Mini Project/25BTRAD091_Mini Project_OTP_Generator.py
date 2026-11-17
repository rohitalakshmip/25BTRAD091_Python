import random

#OTP Generator

def generate_otp(length=6):
    # Generates a random numeric OTP of specified length
    otp = ""
    for _ in range(length):
        otp += str(random.randint(0, 9))
    return otp

print("=== OTP GENERATOR ===")
digits = int(input("Enter length of OTP (e.g., 4 or 6): "))

if digits > 0:
    my_otp = generate_otp(digits)
    print(f"Your generated {digits}-digit OTP is: {my_otp}")
else:
    print("Invalid length!")



    