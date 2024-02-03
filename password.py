import string
import random

def generate_password(length):
    # Combine lowercase, uppercase, digits, and punctuation for a strong password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the length is not greater than the available characters
    length = min(length, len(all_characters))

    # Use random.sample to generate a unique password
    password = ''.join(random.sample(all_characters, length))

    return password

def main():
    try:
        # Prompt the user for the desired length of the password
        length = int(input("Enter the length of the password: "))

        if length <= 0:
            print("Please enter a positive integer for the length.")
            return

        # Generate and print the password using the function
        print("Generated Password:", generate_password(length))

    except ValueError:
        print("Invalid input. Please enter a valid positive integer for the length.")

if __name__ == "__main__":
    main()
