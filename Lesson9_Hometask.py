### TASK 1: Напишіть декоратор, який вимірює і виводить на екран час виконання функції в секундах

# Acceptance criteria:
# 1) function  -> could be any function for the CASE 1, and we can define particular function for the CASE 2
# 2) decorator for the function - need to show the run time of the function 
# 3) decorator has no parameters

## CASE 1: Script for any function (function is of unknown type)

#step 1.1: import the time module
import time
#step 1.2: decorator for the function
def run_time(func):  # decorator
    """Decorator for run time measurement

    Args:
        func (function): function inside the the decoration flow
    """
    def wrapper(*args, **kwargs):
        start_time  = time.time()
        print(f'-->  Before function run time is: {start_time}')
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'-->  After function run time is: {end_time}')
        run_time = end_time - start_time
        return result, print(f'Run_time is: {run_time}')
    return wrapper

# step 1.3: define the function an its decorartion
@run_time
def func(*args, **kwargs):
    """Non defined function
    """    
    print(f'function run is done')
    return 

#step 1.4: call  the function:
func()

## CASE 2: Decorate the function for unpacking the JSON file received from external API provider

# step 2.1: define the function and its decoration
@run_time
def unpack_json(**json_response):
    """Function for unpacking the JSON file
    """
    print(json_response['login'])
    print(json_response['password'])
    
# step 2.2: call the function
json_response = {
    'login': 'User',
    'password': 'fjjs125A',
    'option1': 'debug_mode',
    'validate': True,
    'c': True,
    'abc': [25, 31, 48]
}
unpack_json(**json_response)
    
 

### TASK 2: Напишіть декоратор, який перетворює всі вхідні параметри функції в строки (str) а також перетворює результат роботи функції на строку

# Acceptance criteria:
# 1) function  -> could be any function 
# 2) decorator for the function -> converts function arguments into a string, and converts the function result into a string
# 3) decorator has no parameters

## Script 

#step 1: decorator for the arguments converting
def str_convert(func):  # decorator
    """Decorator: convert each Argument into a string

#     Args:
#         func (function): function inside the the decoration flow
#     """
    def wrapper(*args, **kwargs):
        """Internal function
        Returns:
            _arg_: argument as string
            _kwarg_: argument argument as string
            _res_: result as string
        """        
        for arg in args:
            arg = str(arg)
            print('converted argument positional: ', arg, type(arg))
        for value in kwargs.values():
            v_str = str(value)
            print('converted argument named: ', v_str, type(v_str))
        res = func(*args, **kwargs)
        return res
    return wrapper

#step 2: decorator for the function result converting
def str_result_convert(func):  # decorator
    """Decorator: convert function result into a string

#     Args:
#         func (function): function inside the the decoration flow
#     """
    def wrapper(*args, **kwargs):
        """Internal function
        Returns:
            _arg_: argument as string
            _kwarg_: argument argument as string
            _res_: result as string
        """        
        res = func(*args, **kwargs)
        str_res = str(res)
        return str_res
    return wrapper

#step 3: decorator for the function result converting
@str_convert
@str_result_convert
def func(a, b):
    """Function which returns the sum between arguments

    Args:
        a (_int_): argument 1
        b (_int_): argument 2

    Returns:
        res(_str_): function result
    """    
    res = a + b
    return res

#step 4: call the function with arguments
res = func(1, b = 3)
print(f'Converted function result is: ', res, type(res))

