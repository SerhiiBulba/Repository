## GAME "Rock Paper Scissors Lizard Spock"

from lib import win_rules, get_user_choice, get_computer_choice, get_winner, make_message

def main():
    """MAIN FUNCTION FOR THE GAME 'Rock Paper Scissors Lizard Spock'
    """
    for i in range(1, 4):
        print(f'Try {i}')

        user_choice = get_user_choice()

        computer_choice = get_computer_choice()

        winner = get_winner(user_choice, computer_choice)

        msg = make_message(user_choice, computer_choice, winner)

        print(msg)

main()