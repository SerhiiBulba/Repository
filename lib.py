# ## Functions for the GAME "Rock Paper Scissors Lizard Spock"

from random import choice

def win_rules():
    WIN_RULES = {
    'stone': 'scissors',
    'paper': 'stone',
    'scissors': 'paper',
    'stone': 'lizard',
    'lizard': 'spock',
    'spock': 'scissors',
    'scissors': 'lizard',
    'paper': 'spock',
    'lizard': 'paper',
    'spock': 'stone'
    }
    return WIN_RULES

WIN_RULES = win_rules()

# get data from user
def get_user_choice():
    while True:
        user_choice = input('Enter your choice (stone, paper, scissors, lizard, spock): ')
        if user_choice not in WIN_RULES.keys():
            print('Enter only: stone, paper, scissors, lizard, spock')
            continue
        else:
            return user_choice


# get data from computer
def get_computer_choice():

    computer_choice = choice(list(WIN_RULES.keys()))
    return computer_choice


# define winner
def get_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        msg = 'Draw'
    elif WIN_RULES[user_choice] == computer_choice:
        msg = 'User'
    else:
        msg = 'Computer'

    return msg


# make message
def make_message(user_choice, computer_choice, winner):

    msg = f'User choice is \'{user_choice}\', PC choice is \'{computer_choice}\'. Winner is \'{winner}\''
    return msg


def main():

    for i in range(1, 4):
        print(f'Try {i}')
        user_choice = get_user_choice()

        computer_choice = get_computer_choice()

        winner = get_winner(user_choice, computer_choice)

        msg = make_message(user_choice, computer_choice, winner)

        print(msg)


main()
