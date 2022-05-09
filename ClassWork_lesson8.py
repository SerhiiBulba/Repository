### Feature for definition the messages to the AGE / Код для визначення тексту під кількість років {рік, роки, років}
age = int(input(f'Please, input the age: '))
div_reminder = age % 10

if int(str(age)[-2:]) in (11, 12, 13, 14) or 5 <= div_reminder or div_reminder == 0:
    msg = 'років'
elif div_reminder == 1:
    msg = 'рік'
elif 2 <= div_reminder <= 4:
    msg = 'роки'

print(age, msg)

## Case for the GAME: 'Stone, paper, scissors'
# acceptance criteria:
# objects: [paper, stone, scissors]
# PC can choice  any object - logic of choise is blackbox, could be random
# User can select any object - logic of chois is up to User, could be random
# compare between PC and User choices and define the winner

# Components / Blocks of code:
# Win_Rules: can be the dict
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
    for i in range(1, 4):    # lets have 3 trys for this game: try1, try2 and try3
        print('try {}'.format(i))
        user_choice = get_user_choice()
        pc_choice = get_pc_choice()
        winner = define_winner(user_choice, pc_choice)
        msg = msg_box(user_choice, pc_choice, winner)
        print(msg)

main()


### RECURSION. Factorial
## Recursion - when function calls itself directly or inderectly
counter = 0
def recur_factor(n):
    global counter
    counter += 1
    if n <= 1:
         return 1
    res = n * recur_factor(n - 1)
    
    return res

res = recur_factor(5)
print(res)
print(counter)

counter = 0     # to start counting from 0 we need to place the global variable "counter" right before each function
def rec_fact(n):
    global counter
    counter += 1
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res

print(rec_fact(5))
print(counter)

### FIBONACCI function recursion:
## Example:
counter = 0   # make initial set for counter variable
def fib(n):
    global counter   # define the global variable
    counter += 1     # define the counter - count the number of function run

    if n in (1, 2):
        return 1
        
    fib_rec = fib(n-1) + fib(n-2)
    return fib_rec

print(fib(10))
print(counter)

### FIBONACCI using the cycle, not recursion
counter = 0
def fib_cycle(n):
    
    if n in (1, 2):
        return 1
    global counter
    counter += 1
    fib1 = fib2 = 1
    for i in range(n-2):
        fib1, fib2 = fib2, fib1 + fib2

    return fib2

print(fib_cycle(10))
print(counter)

### IMPORT: rules

#Example 1: need to import only a single function "choice" from module 'random'
from random import choice

## RULES for IMPORTS:

# Rule 1: All imports are always written right in the begining of the file

# Rule 2: If need to import only a single function, then use: from "module_Name" import "function_Name"
from random import randint
print(randint(1,10))

# Rule 3: We can assign the 'alies_name' to imported function / method if we want to have it as individual naming in the code
from random import randint as RI  # where RI - the name of function 'ranint'
print (RI(1, 10))

# Rule 4: if we want to import all functions available in the module, the use '*'. But this is a risk to rewrite some own program names \ 
# by the internal module names, which are not explicit for us
from random import *   # this is a bad practice and recommended not to use it

# Rule 5: we can import the functions from another py.file. If imported several functions, then separate them by coma
# from Lesson7_HomeTask import validate, text_append  # imported 2 functions from the file 'Lesson7_HomeTask.py'
# on real projects classes and functions are located within separate files (libraries), and then being imported

# Rule 6: When importing the file.py, run of all internal code is triggered - Need to keep in mind as it can affect our code
print('before import:')
from Class_Work_lesson7 import foo
print('after import: ')
foo(100)

# Rule 7: If we do not require the whole code triggered by import, we can use mechanism that helps \ 
# to define the Name on which behalf the fucntion is run:
#  --> during the run of any file the variable is created with the name "__name__" 
print(__name__)        # in the file where the code is placed initially, value of the __name__ function is always "main"
#  --> when file is imported then  print(__name__) should return 'file_name'. This case can be used \ 
# for definition whether the file is imported or not
if __name__ == '__main__':  # if the name of file is 'main' then function foo(a) can be run. 
    res = foo(5)            # Here the name is not 'main' so the function returns None
    print(res)
# so need to use the approach above to define, what is required to do for the both cases when file is run itself or the file is imported


    
