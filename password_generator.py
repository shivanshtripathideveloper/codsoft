import random
import string

print("=== PASSWORD GENERATOR ===")

# Take password length input
length = int(input("Enter desired password length: "))

print("\nSelect password complexity:")
print("1. Only Letters")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")

choice = input("Enter choice (1/2/3): ")

# Define character sets
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Decide character pool based on user choice
if choice == '1':
    characters = letters
elif choice == '2':
    characters = letters + digits
elif choice == '3':
    characters = letters + digits + symbols
else:
    print("Invalid choice! Defaulting to Letters + Numbers + Symbols")
    characters = letters + digits + symbols

# Generate password
password = ''.join(random.choice(characters) for i in range(length))

# Display result
print("\nGenerated Password:", password)