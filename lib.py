# ## Functions for the GAME "Rock Paper Scissors Lizard Spock"

from random import choice

def win_rules():
    """Function returns the win_rules
    Returns:
        WIN_RULES (dict): define the list of cases, where User is a winner
    """    
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

def get_user_choice():
    """GET DATA FROM USER
    Returns:
       user_choice (str): User's an input only among: stone, paper, scissors, lizard, spock
    """    
    while True:
        user_choice = input('Enter your choice (stone, paper, scissors, lizard, spock): ')
        if user_choice not in WIN_RULES.keys():
            print('Enter only: stone, paper, scissors, lizard, spock')
            continue
        else:
            return user_choice

def get_computer_choice():
    """GET DATA FROM COMPUTER
    Returns:
       computer_choice (str): random value only among: stone, paper, scissors, lizard, spock
    """
    computer_choice = choice(list(WIN_RULES.keys()))
    return computer_choice


def get_winner(user_choice, computer_choice):
    """DEFINE THE WINNER
    Args:
        user_choice (str): User's input only among: stone, paper, scissors, lizard, spock
        computer_choice (str): Random value among: stone, paper, scissors, lizard, spock
    Returns:
        msg (str): returns the result of Game
    """
    if user_choice == computer_choice:
        msg = 'Draw'
    elif WIN_RULES[user_choice] == computer_choice:
        msg = 'User'
    else:
        msg = 'Computer'

    return msg


def make_message(user_choice, computer_choice, winner):
    """COMPILE THE MESSAGE
    Args:
        user_choice (str): User's input only among: stone, paper, scissors, lizard, spock
        computer_choice (str): Random value among: stone, paper, scissors, lizard, spock
        winner (str): returns the result of Game
    Returns:
        msg (str): compiled message for returning the Game result
    """
    msg = f'User choice is \'{user_choice}\', PC choice is \'{computer_choice}\'. Winner is \'{winner}\''
    return msg



