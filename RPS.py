import random

choices = {
    1: "rock",
    2: "paper",
    3: "scissors"
}

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"

user_wins = 0
computer_wins = 0
ties = 0

print("Welcome to Rock-Paper-Scissors Game!")

while True:
    print("\nChoose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = int(input("Enter your choice (1/2/3): "))

    if user_choice in choices:
        computer_choice = random.randint(1, 3)

        print(f"\nYour choice: {choices[user_choice]}")
        print(f"Computer's choice: {choices[computer_choice]}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_wins += 1
        elif "tie" in result:
            ties += 1
        else:
            computer_wins += 1

        print(f"\nUser wins: {user_wins}")
        print(f"Computer wins: {computer_wins}")
        print(f"Ties: {ties}")

        play_again = input("\nDo you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("Thanks for playing!")
            break
    else:
        print("Invalid choice. Please choose 1 for Rock, 2 for Paper, or 3 for Scissors.")
