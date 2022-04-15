#TASK #1:
# Зформуйте строку, яка містить певну інформацію про символ в відомому слові. 
# Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'". 
# Слово та номер отримайте за допомогою input() або скористайтеся константою. 
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".
#
# ADDITIONAL CHECKS (validation rules) provided within the task:
# inputted word shoud not be empty and should not be alphanumeric 
# inputted seq_number shoud not be empty
# inputted seq_number shoud not exceed the word length 

# print('Please, input the word')
# my_word = input()
# #validation rules for the word:
# len_word = len(my_word)
# if len_word == 0:
#     print('inputted word shoud not be empty, please try again')
# else:
#     if my_word.isalpha() != True:
#         print('word should be alphabetical only')
#     else:
#         print('Please, input the sequense number of character in the word')
# # validation rules for the sequence number of the symbol in the word:
# seq_numb = input()
# len_numb = len(seq_numb)
# if len_numb == 0 or int(seq_numb) <= 0:
#     print('inputted seq_numb shoud not be empty, and more that 0 value')
# else:
# # check if the sequens number exceeds the word length:
#     my_index = int(seq_numb) - 1
#     if my_index <= len(my_word):
#         print('information about the word:')
#         print('The', seq_numb, 'symbol in "', my_word, '" is', '"', my_word[my_index], '"')
#     else:
#         print('character for the inputted sequence number does not exist')

# TASK 2: Ввести з консолі строку зі слів (або скористайтеся константою). Напишіть код, який визначить кількість кількість слів, \
#  в цих даних
my_str = 'ghf jjk dk1 452 26 5s'
print(my_str[len(my_str) // 2::3])
print(type(my_str.split(' ')))
