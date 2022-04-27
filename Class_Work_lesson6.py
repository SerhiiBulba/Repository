# ## Immutable data types: integer, float, boolean, string, None, tuple, frozenset
# a = 2
# print(id(a))
# a += 1
# print(id(a))

# #or

# str_a = 'a'
# print(id(str_a))
# str_a += 'b'
# print(id(str_a))
# print(str_a)

# ## Mutable data types: list, byte array, set, dictionary
# lst = [1, 2, 3]
# print(id(lst))
# lst.append('abc')
# print(lst)
# print(id(lst))

# lst1 = [1, 2, 3]
# lst2 = lst1
# lst2.append('4')
# print(lst1)

# a = "10"
# b = a
# print(b)
# print(id(b))
# b += 'abc'
# print(b)
# print(id(b))

# ## If need to check whether object is True - use operator "is", but not "=="
# ## operator "is" checks whether object ID refers to a specific value
# a = True
# b = False
# if a is a:
#     print(a)
# else:
#     print(b)

# ## OPERATOR "Copy" - provides creation of a new separate object with o copy of data from the old one
# #lets sample:
# lst1 = [1, 2, 3]     #we have object lst:
# lst2 = lst1.copy()   # making a copy
# print(id(lst1))      # print id_lst1
# print(id(lst2))      # print id_lst2, and id_lst1 != id_lst2

# ## !!! but 'COPY' doesn't provide a full copy of totally separated data, for this need to use 'DEEPCOPY'
# ## !!! 'Deepcopy' creates a different object with different structure of data
# ## Lets sample:

# # COPY work:
# lst1 = [1, 2, ['a', 'b']]     #we have object lst:
# lst2 = lst1.copy()            # making a copy
# lst2[2].append('d')            # adding 'c' into the inside list ['a', 'b']
# print(lst1)                   # print id_lst1
# print(lst2)                   # print id_lst2, and id_lst1 == id_lst2

# # DEEPCOPY work:
# import copy
# lst1 = [1, 2, ['a', 'b']]     #we have object lst:
# lst2 = copy.deepcopy(lst1)            # making a copy
# lst2[2].append('d')            # adding 'c' into the inside list ['a', 'b']
# print(lst1)                   # print id_lst1
# print(lst2)                   # print id_lst2, and id_lst1 != id_lst2


# ### FUNCTIONS (procedures)
# ## custom function:

# def function_name(arg1, arg2):
#     res = arg1 + arg2

#     return res
# result = function_name(5, 10)
# print(result)

# ### !!! Rules for functions:
# # 1 function name is separated by underscore '_', and must be MEANINGFUL, recommended name length is 3 words
# # 2 also it is possible to create a fucntion without arguments:
# def add():
#     res = 10 + 10

#     return res
# result = add()
# print(result)


# # 3 function can be without 'return' (but if it is excpected to receive some value from function - then must have 'return'):
# def hello_function():
#     print('Hello')

# hello_function()

# def function_sum(arg1, arg2):   # declaration of the Function
#     result = arg1 + arg2

#     return result

# result = function_sum(20, 30)  # call the function - number of arguments in the call should match their number in declaration
# print(result)

# result = function_sum(20, 50) 
# print(result)

# a = 100
# b = 200
# result = function_sum(a, b)   # call the function using variables. Each variable refers to the appropriate argument of the function
# print(result)

# ## Позиційна передача агрументів:
# result = function_sum(10, 1000)
# print(result)

# ## Іменна передача агрументів:
# result = function_sum(arg2 = 1000, arg1 = 10)
# print(result)

# ## If return is empty or absent, then function returns None

# #1 return is empty:
# def my_fun(a, b, c):
#     res = a * b + c
#     return
# res = my_fun(10,10,10)
# print(res)            # returns None

# #1 return is absent:
# def my_fun(a, b, c):
#     res = a * b + c
# res = my_fun(10,10,10)
# print(res)            # returns None

# ## Комбінована передача аргументів: cспочатку спрацьовує позиційана передача, а потім іменна
# def my_fun(a, b, c):
#     print(f'a = {a}, b = {b}, c = {c}')

# res = my_fun(2, 3, 1)          # result:  a = 2, b = 3, c = 1

# res = my_fun(2, b=3, c=1)          # result:  a = 2, b = 3, c = 1

# ### !!! Priciple of "Single Responsibility": function to do only a single action (and aim a single target)

# ## The Single Responsibility Principle states that “Each software module or class should have only one reason to change“. \
# #  In other words, we can say that each module or class should have only one responsibility to do. \ 
# # So we need to design the software in such a way that everything in a class or module should be related to a single responsibility.

# ## Sample of the function "Greetings":
# def fun_greet(name):
#     msg = (f'Hello, {name.title()} !')

#     return msg     # operator return stops the function

# msg = fun_greet('serhii')
# print(msg)

# ### Sample of the task about age using the function:

# ## Approach 1:
# age = int(input('Input the age'))
# def msg_age(age):
#     if 0 <= age <= 7:
#         return 'Where are the parents ?'
#     elif 7 < age <= 16:
#         return 'Where is the ticket ?'
    
#     return 'Default response'       # if the both checks are failed, then default response to be returned

# print(msg_age(age))

# ## Approach 2:
# age = int(input('Input the age'))
# def msg_age(age):
#     if 0 <= age <= 7:
#         msg = 'Where are the parents ?'
#     elif 7 < age <= 16:
#         msg = 'Where is the ticket ?'
#     else:
#         msg = 'Default response'       # if the both checks are failed, then default response to be returned
    
#     return msg

# print(msg_age(age))

# ### DEFAULT VALUES of variables in the function

# def dev_fun(a, b = 1):  # b = 1 means, that argument 'b' has default values which is '1'
#     dev_val = a / b
    
#     return dev_val

# dev_val = dev_fun(5)    # here we can input only first argument because the second is default
# print(dev_val)

### !!! Do not use Mutable object as default values for arguments
## Bad (incorrect) sample:
def fun_add(number, lst = []):  # this function to add number to the empty list
    lst.append(number)

    return lst

res = fun_add(4)   # function added '4' to the empty list
print(res)
res = fun_add(3)   # function added '3' to the list which includes '4', because argument is a mutable oblect
print(res)
res = fun_add(2)   # function added '2' to the list which includes '4' and '3/, because argument is a mutable oblect
print(res)

## Correct sample:
def fun_add(number, lst=None):  # this function to add number to the empty list
    if lst is None:
        lst = [number]
        return lst
    else:
        lst.append(number)
        
    return lst

res = fun_add(4)   # function added '4' to the empty list
print(res)
res = fun_add(3)   # function added '3' to the empty list, because argument #2 is a None
print(res)
res = fun_add(2)   # function added '2' to the empty list, because argument #2 is a None
print(res)