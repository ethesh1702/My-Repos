import random

def display_rules():
    print("\n--- Welcome to Rock, Paper, Scissors ---")
    print("Rules:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("Type 'exit' anytime to quit the game.\n")
    
def get_player_choice():
    """
    Gets and validates the player's choice.
    """
    while True:
        player_input = input("Choose your weapon (rock, paper, scissors): ").lower()
        if player_input in ['rock', 'paper', 'scissors']:
            return player_input
        else:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

def get_computer_choice_random():
    """"
    Generates a purely random choice for the computer.
    """
    
def get_computer_choice_medium(player_last_move):
    
    if player_last_move is None:
        return get_computer_choice_random() #First round, no history

    # What beats the player's last move?
    if player_last_move == 'rock':
        return 'paper' # Paper beats Rock
    elif player_last_move == 'paper':
        return 'scissors' # Scissors beats Paper
    elif player_last_move == 'scissors':
        return 'rock' # Rock beats Scissors

def determine_winner(player_choice, computer_choice):
   

    if player_choice == computer_choice:
        return 'draw'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return 'player'
    else:
        return 'computer'

def new_func1(player_choice, computer_choice):
    new_func()
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

def new_func():
    """
    Determines the winner of a round.
    Returns 'player', 'computer', or 'draw'.
    """

def play_game():
    """
    Main function to run the Rock, Paper, Scissors game with a medium AI.
    """
    player_score = 0
    computer_score = 0
    round_number = 0
    player_last_move = None # Initialize to store player's previous move

    print("Welcome to Rock, Paper, Scissors (Medium AI Edition)!")

    while True:
        try:
            num_rounds_input = input("How many rounds would you like to play? (Enter '0' for endless mode): ")
            num_rounds = int(num_rounds_input)
            if num_rounds < 0:
                print("Please enter a non-negative number of rounds.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        round_number += 1
        print(f"\n--- Round {round_number} ---")

        player_choice = get_player_choice()
        # Pass the player's last move to the medium AI function
        computer_choice = get_computer_choice_medium(player_last_move)

        winner = determine_winner(player_choice, computer_choice)

        if winner == 'player':
            print("You win this round!")
            player_score += 1
        elif winner == 'computer':
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a draw!")

        print(f"Score: Player {player_score} - Computer {computer_score}")

        # Update player_last_move for the next round
        player_last_move = player_choice

        if num_rounds != 0 and round_number >= num_rounds:
            print("\n--- Game Over! ---")
            if player_score > computer_score:
                print(f"Congratulations! You win the game {player_score} to {computer_score}!")
            elif computer_score > player_score:
                print(f"Too bad! Computer wins the game {computer_score} to {player_score}!")
            else:
                print(f"It's a tie game! {player_score} to {computer_score}!")

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break
            else:
                player_score = 0
                computer_score = 0
                round_number = 0
                player_last_move = None # Reset for new game
                while True:
                    try:
                        num_rounds_input = input("How many rounds would you like to play this time? (Enter '0' for endless mode): ")
                        num_rounds = int(num_rounds_input)
                        if num_rounds < 0:
                            print("Please enter a non-negative number of rounds.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    play_game()