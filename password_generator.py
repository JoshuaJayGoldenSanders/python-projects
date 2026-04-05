import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None
 
    password = "".join(random.choice(characters) for _ in range(length))
    return password

while True:
    print("\n--- Password Generator ---")

    length = int(input("Enter password length: "))

    use_upper = input("Include uppercase letters? (y/n): ").lower() =="y"
    use_lower = input("Include lowercase letters? (y/n): ").lower() =="y"
    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

    if password:
        print("Generated Password:", password)
    else:
        print("You must select at least one character type.")

    again = input("Generate another password? (y/n): ").lower()
    if again != "y":
        print("Goodbye!")
        break
