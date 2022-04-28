## Task #1
## Description: Напишіть функцію, що приймає один аргумант. Функція має вивести на екран тип цього аргумента (використовуйте type)
## Acceptance criteria:
# 1--> function with a single argument
# 2--> function defines the type of the data upon argument
# 3--> input of the data which represents the function argument
# 4--> print the function result


def data_type(arg):
    res = type(arg)

    return res

res = data_type()
print(res)

## Task  #2
## Description: Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float. \
#  Якщо перетворити не вдається функція має повернути 0.
## Acceptance criteria:
# 1--> function with a single argument
# 2--> data type of argument could be any
# 3--> function should return the result which is float type
# 4--> if the type of result is not float, then function should return 0
# 5--> if argument is not inputted, then use some default value and function should return 0 


def my_funct(arg_any='*'):
    try:
        result = float(arg_any)
    except:
        result = 0
     
    return result

result = my_funct([1, 2])
print(result)

## Task #3
## Description: Напишіть функцію, що приймає два аргументи. Функція повинна:
# якщо аргументи відносяться до числових типів - повернути різницю цих аргументів,
# якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
# якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
# у будь-якому іншому випадку повернути кортеж з цих аргументів

## Acceptance criteria:
# 1--> return the difference between arg1 and arg2 if arg1 and arg2 is int or float
# 2--> return the string of concatenated arg1 and arg2 if arg1 and arg2 is string
# 3--> return the dictionary where arg1 = key, arg2 = value, if arg1 is a string and arg2 is not a string
# 4--> return a tuple of arg1 and arg2 for any other data types of function arguments (all cases apart from case 1-3) 

def my_func(arg1=None, arg2=None):
    if ((type(arg1) is int) or (type(arg1) is float)) and ((type(arg2) is int) or (type(arg2) is float)):
        res = arg1 - arg2
    elif (type(arg1) is str) and (type(arg2) is str):
        res = arg1 + arg2
    elif (type(arg1) is str) and (type(arg2) is not str):
        my_dict = {}
        my_dict[arg1] = arg2
        res = my_dict
    else:
        res = (arg1, arg2)
    return res
res = my_func('s', 5)
print(f'The result of function:', res)

