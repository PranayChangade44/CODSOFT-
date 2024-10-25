import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    
    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length - 4)

    
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of the password (minimum 4): "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
