## Функція завершує свою роботу там, де вона зустріла "return"


### DECORATORS - they change the way of function fulfilment not changing it

## Example - I want the function below returns the string, not integer:

# def foo(a, b):

#     return a + b

# ## Lets write the function 'Decorator':

# def fun(a):             # initial function 
#     x = str(a)
#     print(x)
#     return x

# res = fun('I am fun')


def decorator(func):    # start the decoration function

    def inner(*args, **kwargs):      # cover function 'fun' into decorator
        print('Before call function')
        result = func(*args, **kwargs)
        print('After call function')

        return result

    return inner

func = decorator()  # call the decorator for function "fun"
print(func)

# defining a decorator

#### DECORATOR: VERY GOOD SAMPLE

##Step 1
def decorator(func):
 
    # "wrapper" is a Wrapper function in which the argument is called
    # "wrapper" function can access the outer local functions like in this case "func"
    def wrapper():
        print("Hello, this is before function execution")
 
        # calling the actual function now inside the wrapper function.
        func()
 
        print("This is after function execution")
         
    return wrapper

##Step 2
# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")

##Step 3 
# passing 'function_to_be_used' inside the decorator to control its behaviour
function_to_be_used = decorator(function_to_be_used)
# calling the function
function_to_be_used()

##*** We can simplify the step 2 and step 3 by using '@', which is calling the decarotor function:
@decorator
def function_to_be_used():
    print("This is inside the function !!")

function_to_be_used()


### Another case: I want to create the decorator which can return only integer inputs
## Description: we have function (a, b), where result  = a + b. Decorator should wrap the inputs into int/float.

# Step1: define the decorator function:
## Hint: Use the 'isinstance' function. Function isinstance()  returns True if the object is of the specified type, otherwise False.

def only_number(func):
    
    def wrap(*args, **kwargs):
        'print check arguments'
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError('Error1: Args - only integers required')

        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError('Error2: Kwargs - only integers required')
        
        result = func(*args, **kwargs)    # <---- this this the decoration core

        return result 

    return wrap

# Step2: call the decorator function
@only_number
def add_number(a, b):
    print(f'inside function: {a}, {b}')
    return a + b

res = add_number(a = 2, b = 3)
print(res)

###!!! We can wrap the function by several decorators

## Example:
# Step_1: define the Decorator_1
def decorator_1(funct):
    def wrap(*args, **kwargs):
        print('inside decorator_1: start')
        res = funct(*args, **kwargs)
        print('inside decorator_1: end')
        return res
    return wrap
# Step_2: define the Decorator_2
def decorator_2(funct):
    def wrap(*args, **kwargs):
        print('inside decorator_2: start')
        res = funct(*args, **kwargs)
        print('inside decorator_2: end')
        return res
    return wrap
# Step_3: define the function and call the decorator:
@decorator_1
@decorator_2
def funct():
    print('I am a function')
# Step_4: launch the decorated function
funct()  # we receive: start "dec_1", then start "dec_2", then end "dec_2", and then end "dec_1"
         # decorator_2 is run in the first turn, then the decorator_1
         # in other terms: foo() = decorator_1(decorator_2(foo))

### !!! PARAMERIZED DECORATOR: we can have decorator with parameters
##Example: lets decorate the function having the integers only - create the decorater "check_type"

def check_type_decorator(arg_type):    # this decorator checks wether the input is integer

    def first_wrapper(func):         # <--- this decorator pushes the function run

        def second_wrapper(*args):   # <--- this decorator pushes the check run
            print('check arguments')

            for arg in args:         # <--- checking the data type
                if not isinstance(arg, arg_type):
                    raise TypeError('wrong argument')
            result = func(*args)     # <--- returns the function result itself

            return result
        
        return second_wrapper
    
    return first_wrapper

@check_type_decorator(int)      # foo = check_type_decorator(int)(foo)
# step1: check_type_decorator(int) --> first_wrapper
# step2: foo = first_wrapper(foo)

def funct(*args):               
    print(f'I\'m a function')

funct(1)

#####**********  Solving the tasks*************


### TASK 1: create DECORATOR for delaying of function run-time on 10 seconds ahead

## need to use the module "Time"which could be imported

# step 1: create decorator:
import time

def time_sleep(foo):
    def wrapper(*args, **kwargs):
        print('Sleeep-time decorator started')
        time.sleep(2)
        result = foo(*args, **kwargs)
        print('Sleeep-time decorator ended')
        return result
    return wrapper

# step 2: call the decorated function
@time_sleep
def func(*args, **kwargs):
    print(f'Function')

# step 3: run the function which is decorated
print('---> time start:', time.time())
func()
print('---> time end:', time.time())

### TASK 2: USING PARAMETRIZED DECORATOR create the run-time delay of the function by inputting the delay time as parameter

# step 1: create decorator with parameters:

def delay_sec(sec_num):
    def delay(func):
        def wrapper(*args, **kwargs):
            print('Sleeep-time decorator started')
            time.sleep(sec_num)
            result = func(*args, **kwargs)
            print('Sleeep-time decorator ended')
            return result
        return wrapper
    return delay

# step 2: call the decorated function
@delay_sec(5)  # including the parameter: sec_num = 5
def func(*args, **kwargs):
    print(f'Function')

# step 3: run the function which is decorated
print('---> time start:', time.time())
func()
print('---> time end:', time.time())