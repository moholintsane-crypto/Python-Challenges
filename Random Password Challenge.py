import random
import string

def create_password():
    # Prompt for password length
    try:
        length = int(input("Enter password length (e.g., 12-19): "))
    except ValueError:
        print("Invalid input. Using default length 12.")
        length = 12

    # Define character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password securely
    # Using random.SystemRandom().choice provides higher security, as shown in [this Stack Overflow post]
    #(https://stackoverflow.com/questions/7479442/high-quality-simple-random-password-generator) [5].
    password = ''.join(random.choice(characters) for _ in range(length))
    
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    create_password()
