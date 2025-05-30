# Import libraries
import random   # To allow the computer to make random choices
import os       # To clear the terminal screen
import time     # To add delays for better user experience

# Define the main game function
def Start(Score):
    # Clear the terminal screen
    os.system('cls')

    # Prompt the player for their choice and display the current score
    Choice = int(input(f'\n* Score *\nYou: {Score[0]}\nOpponent: {Score[1]}\n\n* Choose *\n1- Rock\n2- Paper\n3- Scissors\nR: '))
    
    # Validate the input to ensure it is between 1 and 3
    while Choice < 1 or Choice > 3:
        Choice = int(input(f'\n* Score *\nYou: {Score[0]}\nOpponent: {Score[1]}\n\n* Invalid choice! *\n1- Rock\n2- Paper\n3- Scissors\nR: '))

    # Computer randomly selects Rock, Paper, or Scissors
    Opponent = random.randint(1, 3)

    # Map the numeric choice to string for display
    if Opponent == 1:
        Response = 'Rock'
    elif Opponent == 2:
        Response = 'Paper'
    else:
        Response = 'Scissors'

    print(f'\nOpponent chose {Response}!')
    time.sleep(2)  # Delay for suspense

    # Determine the outcome of the game
    if Choice == Opponent:
        print('\nIt\'s a tie!')
    elif Choice == 1 and Opponent == 2:
        print('\nYou lost!')
        Score[1] += 1  # Increment opponent's score
    elif Choice == 1 and Opponent == 3:
        print('\nYou won!')
        Score[0] += 1  # Increment player's score
    elif Choice == 2 and Opponent == 1:
        print('\nYou won!')
        Score[0] += 1
    elif Choice == 2 and Opponent == 3:
        print('\nYou lost!')
        Score[1] += 1
    elif Choice == 3 and Opponent == 1:
        print('\nYou lost!')
        Score[1] += 1
    elif Choice == 3 and Opponent == 2:
        print('\nYou won!')
        Score[0] += 1

    # Allow player to return to menu
    Back = int(input('\nType "1" to return\nR: '))
    while Back != 1:
        Back = int(input('\nInvalid option!\nType "1" to return\nR: '))

# Initialize the score: [player, opponent]
Score = [0, 0]

# Main game loop
while True:
    os.system('cls')  # Clear the screen

    # Display menu and prompt for choice
    Menu = int(input(f'\n* Score *\nYou: {Score[0]}\nOpponent: {Score[1]}\n\n* Menu *\n1- Start\n2- Quit\nR: '))
    
    # Validate menu input
    while Menu != 1 and Menu != 2:
        Menu = int(input('\n* Menu *\nInvalid option!\n1- Start\n2- Quit\nR: '))

    # Start game or quit
    if Menu == 1:
        Start(Score)
    else:
        print('\nProgram terminated!')
        break
