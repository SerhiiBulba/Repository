## BASIC PRINCIPLES OF PROGRAMMIN
#1 DRY - do not repeat yourself
#2 KISS - keep it short and simple
#3 YAGNI - You aren’t gonna need it (Developers should start building capabilities only when those capabilities are actually needed, rather than trying to predict future needs. )

#! To keep in mind - any variable represents an object of a particulat class (for instance, string var is an object of class 'string')

# Operators priorities:
# ()
# **
# *  /   //   %
# +   - 
# >   <   >=  <= 
# not
# and
# or 
# =  !=

# # Sample 1
# a = 0
# while a < 100:
#     print (a)
#     a += 1
#     if a > 50:  # limitation for the cycle
#         break   # here break interupts the cycle on 51th element

### Cycle inside another cycle (or incapsulated cycles)
## Sample:
# outer_counter = 0
# while True:
#     print(f'External loop {outer_counter}')
#     outer_counter += 1
    
#     inner_counter = 0
#     while True:
#         print(f'    Internal loop {inner_counter}')
#         inner_counter += 1

#         if inner_counter >= 5:
#             print(f'    Inner loop: end of cycle')
#             break

#     if outer_counter >= 3:
#         print(f'External loop: end of all cycles')
#         break

### Tests: https://www.w3schools.com/python/exercise.asp?filename=exercise_lists4
### About strings         
# 1 If need to check the Data type (for instance: checking whether the data_type is string or not):
# my_str = 'hello'
# if type(my_str) == str:
#     print('it is a string')
# else:
#     print('not a string')
#     print (type(my_str))

## Check the lenght of the string
# my_str1 = 'hello word'
# my_str2 = 'hello world!'
# print(len(my_str1))
# print(len(my_str2))

## Operator "in" -> checks whether one string is included into another one
# if my_str1 in my_str2:
#     print('match')
# else:
#     print('not match')

## function "format" for the string var
# my_str3 = 'How {} You1 {}'
# print(my_str3.format('are','?'))

# if my_str3.find('y'):
#     print('contains int')

# ## function "replace"
# print(my_str3.replace('w', 'WWW'))

# ## function  "strip"  -> for cutting of the string
# var_a = '***Hi***'
# print(var_a.strip('***'))
# print(var_a.lstrip('***'))
# print(var_a.rstrip('***'))

# function "upper", "lower", "title"
# var_b = 'Hello you MY friend'
# print(var_b.upper())
# print(var_b.lower())
# print(var_b.title())

# # function "istitle" -> checks whether the first word starts from the Upper case
# var_c = 'Word'
# if var_c.istitle() == True:
#     print('ok')
# else:
#     print('no')

# function "isalpha", "isdigit", "isalnum" -> checks whether the string contains: only letters / only digits / the both letters and digits
var_d = '4fffd'
if var_d.isalnum() == True:
    print('contains letter and digits')
else:
    print('only digits')