## Task description:
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

### PROGRAM CODE:

## Section 1: Input the list with values of awesome age:
list = [11, 22, 33, 44, 55, 66, 77, 88, 99]

while True:
    try:
        age = int(input(f'Please, input the age:'))
    except:
        print('error 1')
    else:
        if age > 0:
            break
        else:
            print(f'error 2')

## Section 2: Input the text appends:
def year_append(age):
    lst1 = ['1']                           # для додавання: "рік"
    lst2 = ['2', '3', '4']                 # для додавання: "роки"
    lst3 = ['0', '5', '6', '7', '8', '9']  # для додавання: "років"
    age_str = str(age)
    if age_str[-1] in lst1:                # додавання "рік", якщо age закінчується на '1'
        print('рік')
    if age_str[-1] in lst2:                # додавання "роки", якщо age закінчується на '2', '3', '4'
        print('роки')
    if age_str[-1] in lst3:                # додавання "років", якщо age закінчується на '0', '5', '6', '7', '8', '9'
        print('років')

## Section 2: Function: check if the age contains the matched digits (11, 22 ...)
def check_match(age):
    if age in list:
        print('О, вам {} {}! Який цікавий вік!'.format(age, year_append(age)))

    
## Section 3: Function "Return response":
def return_response(age):
    if check_match(age) is True:
        check_match(age)
    elif age < 7:
        print('Тобі ж {}! Де твої батьки?'.format(age))
    elif (age >= 7) and (age < 16) and (age not in list):
        print('Тобі лише {}, а це е фільм для дорослих!'.format(age))
    elif (age >= 16) and (age < 65) and (age not in list):  
        print('Незважаючи на те, що вам {}, білетів всеодно нема!'.format(age))
    elif (age >= 65) and (age not in list):  
        print('Вам {} Покажіть пенсійне посвідчення!'.format(age))
    
return_response(age)















                





