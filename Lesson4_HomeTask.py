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

# 1 input the string
# # 2 validate the inputs
# # 3 find 2 vowels one by one
# # 4 check if it is included into the words
# # 5 count the number of words

# # resolving:



# # 3 find 2 vowels one by one

# ## Define function for cheking the vowels:
# def checkVowels(string):  #use-defined function
#    # check the string contains vowels
#    for char in string:
#       if char in 'aeiouAEIOU':
#          return True
#    return False

# vowel = ['a', 'e', 'i', 'o', 'u']
# my_str = input(f'Input the string: ')
# #1
# for i in my_str:
#     if (checkVowels(my_str) == True):
#         print(my_str.index(vowel))




    


# split the string into the list:
# my_lst = my_str.split()
# print(my_lst)




# lst2 = []

# for i in my_lst:
#     print(i)
    
# for n in i:
#     if n in vowel:
#         x = i.count(n)
#         lst2.append(x)

# print(lst2)



# count letters:
# count_letter = 0
# for letter in my_str:
#     if letter in vowel:
#         count_letter += 1


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

# Step2: validate the inputs:
while True:
    try:
       min_p = float(input(f'Please, input the min price: '))
    except: 
        print('input should be integer or float')
    else:
        break

while True:
    try:
       max_p = float(input(f'Please, input the min price: '))
    except: 
        print('input should be integer or float')
    else:
        break

# Step3: Chek the condition:
print('Match results: ')
for shop, price in shops_dic.items():
    if  min_p < price < max_p:
            print(f'-->', shop)


