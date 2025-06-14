import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if length < 4:
        return "Password length should be at least 4 characters."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("🔐 Welcome to the Password Generator")

length = int(input("Enter password length: "))
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special symbols? (y/n): ").lower() == 'y'

password = generate_password(length, use_upper, use_numbers, use_special)
print(f"\nYour generated password: {password}")
