import random

# Function to generate a password
def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

while True:
    # Get desired password length from the user
    password_length = int(input("Enter the desired password length: "))
    
    if password_length <= 0:
        print("Password length must be a positive integer.")
        
    else:
        # Generate the password using the function
        generated_password = generate_password(password_length)
        
        # Display the generated password
        print("Generated Password : ", generated_password)
        
        # Ask if the user wants to generate more passwords
        again = input("Generate another password? (y/n) : ")
        if again.lower() != "y":
            break
