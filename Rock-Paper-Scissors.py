# just run python3 rock-paper-scissors.py and select one.
# it is set to loop at the bottom when "y" is entered after the result

import random

RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
END = '\033[0m'

def play_game():
    options = ['rock', 'paper', 'scissors']
    user = input(f"{BLUE}Choose rock, paper, or scissors{END}: ")
    computer = random.choice(options)

    print(f'You chose: {BLUE}{user}{END}')
    print(f'I chose: {BLUE}{computer}{END}')

    if user == computer:
        print(f'{GREEN}Tie!{END}')
    elif user == 'rock' and computer == 'scissors':
        print(f'{GREEN}You win!{END}')
    elif user == 'paper' and computer == 'rock':
        print(f'{GREEN}You win!{END}')
    elif user == 'scissors' and computer == 'paper':
        print(f'{GREEN}You win!{END}')
    else:
        print(f'{RED}You lost :({END}')

    play_again = input(f"Do You Want To Play Again? ({GREEN}Y{END}/{RED}N{END}): ")
    if play_again.lower() == 'y':
        play_game()
    else:
        print('Goodbye!')

play_game()
