import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'quit' or 'reset' at any time to exit or restart the game.")
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    
    # Dictionary mapping winning conditions
    # e.g., rock wins against scissors
    wins_against = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    while True:
        # Get user input and convert to lowercase
        player_choice = input("\nEnter your choice (rock, paper, scissors) or type 'quit' or 'reset': ").lower()

        if player_choice == 'quit' or player_choice == 'reset':
            print("Thanks for playing! Goodbye.")
            if player_choice == 'reset' or player_choice == 'quit':
                print("The game has been reset. Scores are now 0-0.")
            break

        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        # Get computer choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Check winner
        if player_choice == computer_choice:
            print(f"Both players selected {player_choice}. It's a tie!")
        elif wins_against[player_choice] == computer_choice:
            print(f"{player_choice.capitalize()} beats {computer_choice}. You win!")
        else:
            print(f"{computer_choice.capitalize()} beats {player_choice}. You lose!")

if __name__ == "__main__":
    play_game()
