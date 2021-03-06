## Task description :
#     Hапишіть программу "Касир в кінотеатрі", яка буде виконувати наступне: Попросіть користувача ввести свсвій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "О, вам <>! Який цікавий вік!"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!"
#     Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік
#     Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача.
#  Наприклад :
# "Тобі ж 5 років! Де твої батьки?"
# "Вам 81 рік? Покажіть пенсійне посвідчення!"
# "О, вам 33 роки! Який цікавий вік!"
# Зробіть все за допомогою функцій! Для кожної функції пропишіть докстрінг.
# Не забувайте що кожна функція має виконувати тільки одну завдання і про правила написання коду.

## Acceptance criteria:
# program provides for  User ability to input the 'age'. Input can be done from string
# need to validate the inputs: 1) only int type  2) not is 0;  3) not is None (empty value)
# return the response including templates (described in the task description)
# includes the docstring documantation for each function

### PROGRAM CODE : ###

"""Section 1: Input the list (global data) with values of awesome age:
"""

list = [11, 22, 33, 44, 55, 66, 77, 88, 99]

def validate():
    """Section 2: Check the input using the cycle

    Returns:
        age: returns the int value of age inputted by User 
    """
    while True:
        try:
            age = input(f'Please, input the age:')
            age_int = int(age)
        except:
            print('Should be integer only, not float, not empty')
        else:
            if age_int > 0:
                break
            else:
                print(f'should be > 0')
    return age

age = int(validate())

"""Section 3: Input the text appends (global data):
"""
def text_append(age):
    lst1 = ['1']                           # для додавання: "рік"
    lst2 = ['2', '3', '4']                 # для додавання: "роки"
    lst3 = ['0', '5', '6', '7', '8', '9']  # для додавання: "років"
    lst4 = ['11', '12', '13', '14', '15', '16', '17', '18', '19']   # для додавання: "років"
    age_str = str(age)
    if age_str in lst4:
        text = 'років'
        return text
    else:
        if (age_str[-1] in lst1):                # додавання "рік", якщо age закінчується на '1'
            text = 'рік'
            return text
        elif (age_str[-1] in lst2):                # додавання "роки", якщо age закінчується на '2', '3', '4'
            text = 'роки'
            return text
        elif (age_str[-1] in lst3):                # додавання "років", якщо age закінчується на '0', '5', '6', '7', '8', '9'
            text = 'років'
            return text

text = text_append(age)

def check_match(age):
    """Section 4: FUNCTION "check if the age contains the matched digits (11, 22 ...)
    Args:
        age (str): age of the Customer
    """    
    if age in list:
        print('О, вам {} {}! Який цікавий вік!'.format(age, text))

    
def return_response(age):
    """Section 5: FUNCTION "Return response":
    Args:
        age (str): age of the Customer
    """    
    if check_match(age) is True:
        check_match(age)
    elif age < 7:
        print('Тобі ж {} {}! Де твої батьки?'.format(age, text))
    elif (age >= 7) and (age < 16) and (age not in list):
        print('Тобі лише {} {}, а це е фільм для дорослих!'.format(age, text))
    elif (age >= 16) and (age < 65) and (age not in list):  
        print('Незважаючи на те, що вам {} {}, білетів всеодно нема!'.format(age, text))
    elif (age >= 65) and (age not in list):  
        print('Вам {} {}. Покажіть пенсійне посвідчення!'.format(age, text))
    
return_response(age)















                





