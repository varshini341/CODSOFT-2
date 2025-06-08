import random
import string

def generate_password(length):
    # Define the character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password from the character set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Generated Password: {password}")

# Run the main function
if __name__ == "__main__":
    main()
