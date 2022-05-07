# ### Feature for definition the messages to the AGE / Код для визначення тексту під кількість років {рік, роки, років}
# age = int(input(f'Please, input the age: '))
# div_reminder = age % 10

# if int(str(age)[-2:]) in (11, 12, 13, 14) or 5 <= div_reminder or div_reminder == 0:
#     msg = 'років'
# elif div_reminder == 1:
#     msg = 'рік'
# elif 2 <= div_reminder <= 4:
#     msg = 'роки'

# print(age, msg)

### Case for the GAME: 'Stone, paper, scissors'
## acceptance criteria:
# objects: [paper, stone, scissors]
# PC can choice  any object - logic of choise is blackbox, could be random
# User can select any object - logic of chois is up to User, could be random
# compare between PC and User choices and define the winner

## Components / Blocks of code:
#1 Win_Rules: can be the dict
# Let's consider that 'key' should be the User_Choice
# Let's consider that the dict should be the CONSTANT (constants are always in upper case)

from secrets import choice   # function choice selects random value from the object that can be indexed (list, string)


WIN_RULE = {
    'scissors': 'paper',
    'stone': 'scissors',
    'paper': 'stone'
}
# 1 Get User_Choice
def get_user_choice():
    while True:
        user_choice = input(f'Input the choice: paper, stone, scissors:  ')
        if user_choice not in WIN_RULE.keys():
            print(f'Enter only scissors, paper or stone')
            continue
        else:
            return user_choice

# user_choice = get_user_choice()

# 2 Get PC_Choice
def get_pc_choice():
    pc_choice = choice(list(WIN_RULE))   ## need to transform the dict WIN_RULE into the list, as choice can work with list
    return pc_choice

# pc_choice = get_pc_choice()

# 3 Compare the choices
def define_winner(user_choice, pc_choice):
    if user_choice == pc_choice:
        winner = 'Draw'
    elif WIN_RULE[user_choice] == pc_choice:
        winner = 'User'
    else:
        winner = 'PC'
    return winner

# 4 Return the msg
def msg_box(user_choice, pc_choice, winner):
    msg = f'User choice is \'{user_choice}\', PC choince is \'{pc_choice}\', winner is \'{winner}\''
    return msg

# 5 Main function:

def main():
    user_choice = get_user_choice()
    pc_choice = get_pc_choice()
    winner = define_winner(user_choice, pc_choice)
    msg = msg_box(user_choice, pc_choice, winner)
    print(msg)

main()


