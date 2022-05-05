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

## Section 1: providing user inputs

print('Please, input the age:', input(int))


## Section 2: validate the inputs

## Section 3: dictionaries for response-template (global)

## Section 4: check if the age contains the matched digits (11, 22 ...)
