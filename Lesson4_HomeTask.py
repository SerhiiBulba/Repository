## Перепрошую
#  я почав розбиратися з ДЗ, але не вистачило часу, трохи заплутався
#  не заклав спочатку достатнього запасу і хочу взяти ще час, аби завершити роботу
#  витратив час, однак поки що не виходить завдання 1
#

# TASK 1: Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів, \
# які містять дві голосні літери підряд.
# ACCEPTANCE CRITERIA:
# GIVEN: - have inputs of any string via console
#   and: - the string can include any characters 
#  WHEN: - push the code
#  THEN: - search the word where 2 vowels come one by one 
#   and: - count the number of words

#####  resolving:

# Step 1: Provide initial inputs
## 1.1 Input the string and validate it is not empty:
while True:
    my_str = input(f'Please, input the string: ')
    if len(my_str) != 0:
        print('The number of words with coupled vowel letters is: ')
        break
    else:
        print('string should not be empty')

## 1.2 Input the list of vowels:
vowel = ['a', 'e', 'i', 'o', 'u']

# Step 2: Processing the inputs
## 2.1 Set the cycle for check out whether letters are vowels:
for letter in vowel:

## 2.2 Set the cycle replacing the vowel letters onto '*':
    if letter in my_str:
        my_str = my_str.replace(letter, '*')

## 2.3 Create the interim list #1 from the string:
my_lst = list(my_str.split(' '))

## 2.4 Create the interim list #2 for storing the data processed:
f_lst = []

## 2.5 Set the cycle for cheking whether the element in the list contains '**' ('**' -> means the vowel letters are one by one):
for word in my_lst:
    if '**' in word:
        f_lst.append(word)

# Step 3: Print the result:
print(len(f_lst))


### TASK 2: Є два довільних числа які відповідають за мінімальну і максимальну ціну. \ 
# Є Dict з назвами магазинів і цінами: \ 
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, \ 
# "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "sota": 37.720, "rozetka": 38.003}. \ 
# Напишіть код, який знайде і виведе на екран назви магазинів, \ 
# ціни яких попадають в діапазон між мінімальною і максимальною ціною.

# Step1: input the shops dictionary:
shops_dic =  {
     "cito": 47.999,
     "BB_studio": 42.999,
     "momo": 49.999,
   "main-service": 37.245,
    "buy.now": 38.324,
     "x-store": 37.166,
      "the_partner": 38.988,
       "sota": 37.720,
        "rozetka": 38.003
    }

# Step2: validate the inputs for min and max price:
while True:
    try:
       min_p = float(input(f'Please, input the MIN price: '))
    except: 
        print('Error message 1: min price should be integer or float, try again')
    else:
        if min_p > 0:
            break
        else:
            print('Error message 2: MIN price should value > 0, try again')
            continue
while True:
    try:
        max_p = float(input(f'Please, input the MAX price: '))
    except: 
        print('Error message 3: MAX price should be integer or float, try again')
    else:
        if max_p > 0:
            break
        else:
            print('Error message 4: MAX price should value > 0, try again')
            continue
    finally:        
        if max_p > min_p:
            break
        else:
            print('Error message 5: MAX price should exceed the MIN price, try again')
            continue
    
# Step3: Chek the condition and show results:
print('Match results: ')
for shop, price in shops_dic.items():
    if  min_p < price < max_p:
        print(f'-->', shop)




