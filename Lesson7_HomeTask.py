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

## Section 1: user inputs (global) and validate them:
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
         
print(type(age))

## Section 2: check if the age contains the matched digits (11, 22 ...)
def check_match(age):
    if len(str(age)) == 2:
        if str(age)[0] == str(age)[1]:
            print('О, вам {}! Який цікавий вік!'.format(age))
    
check_match(age)




# a = '1'
# b = '2'
# c = '3'

# print("Character at index {} in the string '{}' is {}.".format(a, b, c))


## function "format" for the string var
# my_str3 = 'How {} You1 {}'
# print(my_str3.format('are','?'))


                






## Section 3: dictionaries for response-template (global)

## Section 4: 
