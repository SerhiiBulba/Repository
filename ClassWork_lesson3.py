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

print('Please, input the word')
my_word = input()
#validation rules for the word:
len_word = len(my_word)
if len_word == 0:
    print('inputted word shoud not be empty, please try again')
else:
    if my_word.isalpha() != True:
        print('word should be alphabetical only')
    else:
        print('Please, input the sequense number of character in the word')
# validation rules for the sequence number of the symbol in the word:
seq_numb = input()
len_numb = len(seq_numb)
if len_numb == 0 or int(seq_numb) <= 0:
    print('inputted seq_numb shoud not be empty, and more that 0 value')
else:
# check if the sequens number exceeds the word length:
    my_index = int(seq_numb) - 1
    if my_index <= len(my_word):
        print('information about the word:')
        print('The', seq_numb, 'symbol in "', my_word, '" is', '"', my_word[my_index], '"')
    else:
        print('character for the inputted sequence number does not exist')

# Класна робота: 
my_str = 'ghf jjk dk1 452 26 5s'
print(my_str[len(my_str) // 2::3])
print(type(my_str.split(' ')))

my_list = ['a', [2,7], 'fjd',  25]
print(my_list)

# Capitalizing:
print(my_list[0].capitalize())
print(my_list[0:2])

# Adding a new element to the list:
my_list.append('hfhdjd2')

# Removing a new element from the list:
my_list.remove('a')
print(my_list)

# Removing the element from the list by the index of this element:
my_list.pop(0)
print(my_list)

# Replacing the element in the list using index:
my_list[0] = my_list[-1]
print(my_list)

# Replacing several elements in the list by pointing out their indexes:
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)

res = my_list + [2, 3]
print(res)

# Replacing the list-element inside the list:
my_list = [['g', 'b'], [2,7], [5, 7, 9], [5]]
print(my_list)
my_list[-1][-1] = 'abc'
print(my_list) # result will be: [['g', 'b'], [2, 7], [5, 7, 9], ['abc']]

# COMPARIZON of the lists - we can compare only for equality
my_list1 = [1, 2, 3]
my_list2 = [1, 2, 3]
my_list3 = [3, 2, 3]
print(my_list1 == my_list2)
print(my_list1 == my_list3)
print(my_list1 < my_list3)

## Using check of BOOLEAN for lists: if list contains even a single value - then True, if not - then False
my_list1 = [1]
my_list2 = []
print(bool(my_list1)) # True
print(bool(my_list2)) # False


# Convertion the string to the list:
my_str = '123'
print(list(my_str))

# TUPLE - data type
my_tup = (1, 2, 3)
print(my_tup)
print(my_tup[1])
print(my_tup[0:1])
# my_tup[2] = 10   # changes are not supported for the tuples

## Operations with tuples:
my_tup1 = (1, 2, 3)
my_tup2 = (1, 2, 3)
my_tup3 = my_tup1 + my_tup2
print(my_tup3)
my_tup3 = my_tup1 * 3
print(my_tup3)

# Lists inside the tuples:
my_tup1 = (1, 2, [1, 2])
my_tup1[-1].append('[1, 2, 3]')
print(my_tup1)

## We can change the tuple to list and vice versa:
my_list = list(my_tup1)
print(type(my_list))

# Function Try / Expet  -> try to perform some action and provide response if error occured
# Sample 1 "A sibgle error"
try:
    age = int(input('Please, input the age'))  # !!! Do not include into the block "try" a whole logic, but only the case which is possible failed with error
except:
    print('error')
# when we remain empty row - that means the code followint to process from the row after
print('next code', age)

# Sample 2 "Several errors"
try:
    age = int(input('Please, input the age: '))
except ValueError:
    print('not an integer')
except ZeroDivisionError:
    print('not a zero')
except SyntaxError:
    print('not empty')

print('good', age, 'is your age')

# Sample 3 "Several errors + store each on einto specific object"
try:
    age = 10 / int(input('Please, input the age: '))
except ValueError as e:
    print('not an integer', e.args)
except ZeroDivisionError as e:
    print('not a zero', e.args)
except SyntaxError as e:
    print('not empty', e.args)
except Exception as e:
    print('unknown error', e.args)

print('good', age, 'is your age')

## Sample 4: Using 'try' + 'except' + 'else;'
# try -> check an error -> if error is not occured, then go to 'else'
# this is a sample of some cycle
# it is used when action is taken depends on whether the error occured or not
try:
    age = 10 / int(input('Please, input the age: '))
except ValueError as e:
    print('not an integer', e.args)
except ZeroDivisionError as e:
    print('not a zero', e.args)
except SyntaxError as e:
    print('not empty', e.args)
except Exception as e:
    print('unknown error', e.args)
else:
    print('no exception')
    print(age)

print('next code')

# Sample: 5 when using 'try' + 'except' + 'else' + 'finally'
# 'finally' is used for the case when we need an action regardless the error occured or not
# 'finally' is used for instance when need to close the connection even in case, when error occured
try:
    age = 10 / int(input('Please, input the age: '))
except ValueError as e:
    print('not an integer', e.args)
except ZeroDivisionError as e:
    print('not a zero', e.args)
except SyntaxError as e:
    print('not empty', e.args)
except Exception as e:
    print('unknown error', e.args)
else:
    print('no exception')
    print(age)
finally:
    print('close connection')

## Sample: If we need to combine a range of errors for a single error-response, we can combine them in the next way:
try:
    age = 10 / int(input('Please, input the age: '))
except (ValueError, ZeroDivisionError, SyntaxError) as e:
    print('Valuer error, devision by zero or syntax error', e.args)

print('next code')


### Cycle "FOR" ("FOREACH")
# for cases when we need to pass the collection by each element
# !!! by the way - in Python there are 3 data_types which could be indexed: 'string', 'list', 'tuple'
my_list = ['a', [2,7], 'fjd',  25]
for i in my_list:
    print(i)
    print(type(i))

#OR:
my_str = 'jfsjkl_jfskjrrn142'
for i in my_str:
    print(i)
    print(type(i))

# #OR:
name_list = ['Tom', 'Anna', 'Greg']
for name in name_list:
    print(name)
    print(type(name))

#OR:

name_list = ['Tom', 'Anna', 'Greg', 'R', 'Tom']
surname_list = ['Brok', 'Loon', 'Sun']
for name in name_list:
    for surname in surname_list:
        print(name + ' ' + surname)
        
#OR:
name_list = ['Tom', 'Anna', 'Greg', '', 'Tom']
for name in name_list:
    print(name)
    if len(name) <= 1:
        break

### If need to have some limitation for the cycle "FOR", we use the function "Range"
# "Range(n)" creates the iterator which counts the cycle withib 0-n iterations
name_list = ['Tom', 'Anna', 'Greg', 'Rol', 'Tom', 'Ball']
for name in range(3):
    print(name)

        

