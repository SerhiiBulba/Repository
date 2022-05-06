# ## !!! Variable which is defined in the function exists only inside this function and no outside
# a = 100

# def foo(x):
#     print(x)

#     return

# res = foo(a)

# ## NAME SPACE (область видимості змінних): There are several levels of Name_Spaces in Python:

# # ... built-in   - all default built-in names of commands and functions of Python
# # ......global   - the variables and constants in the pythin file
# # .........local - all variables inside the function

# #  But if the variable is absent inside the function (local), then the function is looking for this variable in global when run
# # Priorities for search: 1 - local, 2 - global, 3 - built-in
# # Despite the availability of the variable outside the function can only read this variable and no more action
# # Why external variable is readable  - this prevents from unexcpected changes of this external variable by another function (User)
# # !!! So always need to set variables through the function arguments only (in other words - inside the function). |
# # But CONSTANT should be set as Global

# ## Approach GLOBAL for override the readable status of variable inside the function

# a = 10

# def spam(x):
#     print(x)
#     x += 20

#     return x

# print('before function run:', a)
# a = spam(a)          # this is visible declaration / явне оголошення про глобальну змінну - в функцію покладу значення глобальної змінної а=10
# print('after function run:', a)

# ### How to convey uncertain number of postitional arguments (for instance, if smth passing from frontend to backend - the number of aguments could be different)
# # Позиційна передача довільної кількості аргументів "args"

# #  Use the operator '*args' - it returnes the tuple with defined arguments
# Example:

# def function(*args):  # for each set of any arguments the function returnes a tuple
#     print(type(args)) 
#     print(args[0])    # we can retrive the argument by index

# print(function(1, '3', 3))
# print(function(2, 5, 7, [3]))

# # We can combine the 'args' with other arguments. This could be used for filtration the data
# Example:

# def function (arg1, arg2, *args):  # here we have 2 defined arguments and all other should be undefined
#     print(arg1, arg2)   #here print two first arguments which are defined -> tuple (1, 'a')
#     print(args)  #here print all other uncertain arguments  -> tuple (1, 2, 3)

# function(1,'a', 1, 2, 3)

# ## Also we can unpack the set of data in list using '*'
# # Example:

# def function(arg1, arg2, *args):
#     print(arg1, arg2)
#     print(args)

# data = [1, 2, 3, 4, 5]   # list from data

# function(*data)              # function returns 1 2 ... , so it retrives two arguments from the list data

# ## Як передати довільну кількість Іменованих аргументів - іменна передача через функцію "**kwargs"
# ## This approach returnes argumnets with their values in form of dictionary
# # Exmaple 1:
# def function(**kwargs):
#     print(type(kwargs))
#     print(kwargs)

# function(x1 = 1, x2 = 2, x3 = 3)

# # Exmaple 2:
# def function2(x1, x2, **kwargs):
#     print(x1, x2)
#     print(kwargs)

# function2(x1 = 1, x2 = 2, x3 = 3, x4 = 'abc')

# ## Unpack the dictionary into function:
# #Example 1:
# data_dict = {
#     'a': 1,
#     'b': 2,
#     'c': 'a'
# }
# def function(**kwargs):
#     print(kwargs)

# function(**data_dict)

# #Example 2:
# data_dict = {
#     'login': 1,
#     'password': 2,
#     'c': 'a',
#     'd': 0
# }
# def function(login, password, **kwargs):  # via this function we retrieve the login and password, other data are put into separate dictionary
#     print(login, password)
#     print(kwargs)

# function(**data_dict)

# ## COMBINED '*args' and '**kwargs'
# def function(*args, **kwargs):

#     print(args)
#     print(kwargs)

# function(1, 2, 3, 4, a = 1, b = 5, c = 'abc')

# # Case when need to retrieve the parameter from the dictionary (API response)
# # Example: 
# # API sends json response which could be formatted into dictionary:

# def unpack_json(**json_response):

#     print(json_response['login'])
#     print(json_response['password'])
    
# json_response = {
#     'login': 'User',
#     'password': 'fjjs125A',
#     'option1': 'debug_mode',
#     'validate': True
# }

# unpack_json(**json_response)

# ## When the function changes the list:
# def function(lst):
#     print(id(lst))
#     print(lst)
#     lst.append('abc')

#     return lst

# lst  = [1, 2, 3]
# res  = function(lst)
# print(res)
# print(id(res))

# ### TYPE HINTING: when we can point out some hints inside the function

# ## TYPE 1: hints in function declaration:

# def function(a: int, b: str):  # here: we can use the Colon (:) right after variable name: 'var': 'data type'
#     print(a, b)

#     return a, b

# # res = function('as', 5)

# ## ALSO WE CAN DERIVE THE INFO about function annotation / info using HELP or ANNOTATION

# print(function.__annotations__)
# help(function)

# ## TYPE 2: Doc String:

# def function(a, b):
#     """ Doc_String: this function exponentiates the argument 'a' by argument 'b' """
#     res = a ** b
#     print(res)

#     return res

# function(5, 2)

# # ## We can call the Doc_String using the 'Magic': __doc__

# print(function.__doc__)

# ## TYPE 3: Doc_String(style: restructured text) + Type_Hinting:

# def function(a, b, c):
#     """ restructured text style:

#     ;parameter a: description
#     ;type a: int
#     ;parameter b: description
#     ; type b: str
#     ; parameter c: description
#     ; type c: bool
#     """
#     print(a, b, c)

# function(5, {}, 15)

# # Call the hints:
# help(function)
# print(function.__doc__)

# def fun(a):
#     """_summary_

#     Args:
#         a (int): _description_

#     Returns:
#         _type_: _description_
#     """
#     print(a)

#     return a

# help(fun)

def text_append(age):
    lst1 = ['1']                           # для додавання: "рік"
    lst2 = ['2', '3', '4']                 # для додавання: "роки"
    lst3 = ['0', '5', '6', '7', '8', '9']  # для додавання: "років"
    lst4 = ['11', '12', '13', '14', '15', '16', '17', '18', '19']   # для додавання: "років"
    age_str = str(age)
    if age_str in lst4:
        text = 'років'
        return text
    else:
        if (age_str[-1] in lst1):                # додавання "рік", якщо age закінчується на '1'
            text = 'рік'
            return text
        elif (age_str[-1] in lst2):                # додавання "роки", якщо age закінчується на '2', '3', '4'
            text = 'роки'
            return text
        elif (age_str[-1] in lst3):                # додавання "років", якщо age закінчується на '0', '5', '6', '7', '8', '9'
            text = 'років'
            return text

text = text_append(age)



