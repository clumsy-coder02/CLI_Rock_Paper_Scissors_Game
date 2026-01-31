# modules used
import random
import getpass # hide input from the terminal

# game intro
print() # spacing
print("Rock🪨,Paper📃,Scissors✂️")
print() # spacing

# game options
print("\nEnter 1 for:Player vs Machine\nEnter 2 for:Player vs Player\nEnter 3 for:Exit")

print() # spacing
# select from the options 
user_choice = int(input("Select an option from the above(1-3): "))

# game options, the main function
def game_options():
    if user_choice == 1: # call the player vs machine function
        player_machine()
    elif user_choice == 2: # call the player vs player function
        player_player()
    elif user_choice == 3: # call the exit game function
        exit_game()
    else: 
        print("Select an option by typing the number")


print() # spacing
# player vs machine function
def player_machine():
    print("Your Selection: Player vs Machine")
    print() # spacing

    # list order = ["Rock","Paper","Scissors"]

    # list of options & selections
    options = ["Rock","Paper","Scissors"] # don't change the order of the list
    player_name = input("Enter your name: ") # enter name
    # selections
    print() # spacing
    print("'Enter a number to choose'")
    player = int(input("Enter 1 for; Rock\nEnter 2 for; Paper\nEnter 3 for; Scissors: ")) # select choice
    machine = random.randint(1,3) # random selection

    # Rock beats Scissors, Scissors beats Paper, Paper beats Rock, a tie if they're the same

    # game logic
    if player == machine: # tie,if they're the same
        # minus 1 from selections to match indices of the list
        print() # spacing
        print(f"A tie!; {player_name}: {options[(player - 1)]}, Machine: {options[(machine - 1)]}")
    elif player > machine: # player wins, condition depends on the order of the list
        # minus 1 from selections to match indices of the list
        print() # spacing
        print(f"{player_name} wins!; {player_name}: {options[(player - 1)]}, Machine: {options[(machine - 1)]}")
    elif machine > player: # machine wins, condition depends on the order of the list
        # minus 1 from selections to match indices of the list
        print() # spacing
        print(f"Machine wins!; {player_name}: {options[(player - 1)]}, Machine: {options[(machine - 1)]}")


print() # spacing
# player vs player function
def player_player():
    print("Your Selection: Player vs Player")
    print() # spacing

    # list of options & selections
    options = ["Rock","Paper","Scissors"]

    # enter names for recognition
    player_one_name = input("Player One: Enter your name: ")
    print()  # spacing
    player_two_name = input("Player Two: Enter your name: ")
    print()  # spacing

    print("\"There's no fun if you see what your opponent selected\"")
    # display options
    print("\nEnter 1 for; Rock\nEnter 2 for; Paper\nEnter 3 for; Scissors")
    print()  # spacing
    # selections
    player_1 = int(getpass.getpass(f"{player_one_name}; Enter a number to choose(1-3): "))
    print() # spacing

    print("\"There's no fun if you see what your opponent selected\"")
    # display options
    print("\nEnter 1 for; Rock\nEnter 2 for; Paper\nEnter 3 for; Scissors")
    print()  # spacing
    player_2 = int(getpass.getpass(f"{player_two_name}; Enter a number to choose(1-3): "))

    # Rock beats Scissors, Scissors beats Paper, Paper beats Rock, a tie if they're the same

    # game logic
    if player_1 == player_2: # a tie
        # minus 1 from selections to match indices of the list
        print() # spacing
        print(f"A tie!; {player_one_name}: {options[(player_1 - 1)]}, {player_two_name}: {options[(player_2 - 1)]}")
    elif player_1 > player_2: # player_1 wins
        # minus 1 from selections to match indices of the list
        print() # spacing
        print(f"{player_one_name} wins!; {player_one_name}: {options[(player_1 - 1)]}, {player_two_name}: {options[(player_2 - 1)]}")
    elif player_2 > player_1: # player_2 wins
        # minus 1 from selections to match indices of the list
        print() # spacing
        print(f"{player_two_name} wins!; {player_two_name}: {options[(player_2 - 1)]}, {player_one_name}: {options[(player_1 - 1)]}")

# exit function
def exit_game():
    exit()

# what function to call first,
# at the start of the program
if __name__ == "__main__":
    game_options()

