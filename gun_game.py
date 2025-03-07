import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    
    # Losing conditions
    if (player_choice == 0 and computer_choice == 1) or \
       (player_choice == 1 and computer_choice == 2) or \
       (player_choice == 2 and computer_choice == 0):
        return "You lose!"

    # Winning conditions
    return "You win!"

# Main game loop
def play_game():
    print("Welcome to Snake, Water, Gun!")
    print("Choices: 0 - Snake, 1 - Water, 2 - Gun")

    while True:
        # Player input
        player_choice = input("Enter your choice (0/1/2): ")
        if player_choice not in ["0", "1", "2"]:
            print("Invalid choice, please choose either 0, 1, or 2.")
            continue

        player_choice = int(player_choice)  # Convert to integer
        computer_choice = random.randint(0, 2)  # Computer chooses randomly
        
        # Display choices
        choices = ["Snake", "Water", "Gun"]
        print(f"You chose: {choices[player_choice]}")
        print(f"Computer chose: {choices[computer_choice]}")
        
        # Determine and display the winner
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

# Run the game
play_game()
