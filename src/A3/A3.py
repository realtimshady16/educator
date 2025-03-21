import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    """
    Generates a random password based on specified criteria.

    Args:
        length: The desired length of the password.
        use_uppercase: Whether to include uppercase letters.
        use_lowercase: Whether to include lowercase letters.
        use_digits: Whether to include digits.
        use_symbols: Whether to include symbols.

    Returns:
        A randomly generated password as a string, or None if no character sets are selected.
    """

    character_sets = []

    if use_uppercase:
        character_sets.append(string.ascii_uppercase)
    if use_lowercase:
        character_sets.append(string.ascii_lowercase)
    if use_digits:
        character_sets.append(string.digits)
    if use_symbols:
        character_sets.append(string.punctuation)

    if not character_sets:
        return None  # No character sets selected

    all_characters = "".join(character_sets)
    password = "".join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
        use_digits = input("Include digits? (y/n): ").lower() == "y"
        use_symbols = input("Include symbols? (y/n): ").lower() == "y"

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)

        if password:
            print("Generated password:", password)
        else:
            print("Please select at least one character set.")

    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()