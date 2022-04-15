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

# my_word = input('Please, input the word: ')
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

#TASK #2: Ввести з консолі строку зі слів (або скористайтеся константою). Напишіть код, який визначить кількість  слів, \
# в цих даних
my_str = input('Please, input the string: ')
x = my_str.split(' ')
print('', len(x))

# TASK #3: 3.	Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. \
#  Напишіть механізм, який сфлрмує новий list (наприклад lst2), який би містив всі числові змінні, які є в lst1. \ 
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску. 


