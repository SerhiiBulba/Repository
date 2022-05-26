### OBJECT ORIENTED PROGRAMMING (OOP)

# *--------PRINCIPLES OF OOP---------*

# --> [1] Abstraction
# its about absract vision about the object that exists in real world
# we take from the object only what we need for the Programm

# --> [2] Encapsulation
# its ability of data allocation and methods this data processing within a single object
# encapsulation  - classifying the methods within the object by Private and Public

# --> [3] Inheritance
# when some object can inherit the properties from another one
# when 'class_auto' can inherit properties from 'class_weekle'  - it helps to save the resources when creating a new code

# --> [4] Polymorphism
# ability of programm to interact with object of different classes
# when function can process data 
# in different ways in case when data may have different types
# so the function can run with any type of data
# ad-hock polymorphism in Python - when methods and functions run with the references to objects, not to object directly
# on the OOP context polymorphism  - the behaviour of the programm to run with objects of different types

# --> [5] Single Responsibility
# function or class does only a single task


## CLASSES and OBJECTS

## {!!!} As usual classes are creaded for separating the functionality:
for instance: we create classes 'Customer', 'Goods', 'DateTime' for storing transactional info within the class 'Transaction'
# Class 'Transaction' is multiply inherited from the classes 'Customer', 'Goods' and 'DateTime'
# Difference between 'class' and 'object':
# _-> 'class'   is the scheme for object projecting / creating. Class defines the object attributes (properties) and methods (behaviour)
# --> 'object' is the implementation of the class itself by some functionality. "object' is also the result of the class run

# # wneh create a new class - need:
# class ClassName:
#    pass

# print(ClassName)

# # when create an object:

# object = ClassName()
# print(object)
# print(type(object))

# # when need to define if the 'object' belongs to the class 'ClassName'

# print(isinstance(object, ClassName))   # expecting to receive the 'true'

### CREATING THE OBJECT and ITS METHOD INSIDE (abstraction)

class AbstractUser:
    name = 'Serg'
    age = '38'  
    def say_hello(self, word):   # 'self' - is just the name of object in 'MyClass'. Could use any name
        return f'{word}, my name is {self.name} and I am {self.age} years'


## call to the object and retrieve the value using '.'
myObject = AbstractUser()
print(myObject.name)
print(myObject.age)

## call the method 'myClassMethod'
user1 = AbstractUser()   # !!! it is strongly required to create the object 'user1' before the next call 'userHello'. 
# --> object 'user1' should inherit the class 'AbstractUser'

userHello = user1.say_hello(word = 'Hello')  # here I add value to the argument 'word' = 'Hello'
print(userHello)

# OR we can call the class and method inside it:
userHi = AbstractUser.say_hello(user1, word = 'Hello')  # user1.say_hello()  = AbstractUser.say_hello(user1)
print(userHi)

## I can rewrite the attribute of an object - for example, lets rewrite 
user1.name = 'Mark'
userHello = user1.say_hello(word = 'Hello')
print(userHello)

### WE CAN DEFINE INITIAL STATE OF THE OBJECT using__init__ magic method  (encapsulation)
## __init__ method requires to define initial values of arguments when an object created

# Step 1: define the class and objest
from re import A


class AbstractUser:
    name = 'Serg'
    age = '38'  
    def __init__(self, initial_name, initial_age):  # 'self' --> the object initialization wich is called when function is running
        # '_init_' --> is used modification the object state 
        print(self.name, self.age)
        self.name = initial_name
        self.age = initial_age

    def say_hello(self, word):   # 'self' - is just the name of object in 'MyClass'. Could use any name
        return f'{word}, my name is {self.name} and I am {self.age} years'


# Step 2: call to the object and retrieve the value using '.'
user1 = AbstractUser(initial_name = 'Bob', initial_age = 20)  # for any case if even rewrite the argument, we'are get initial values only
userHello = user1.say_hello(word = 'Hello')
print(userHello)
# Step 3: define new names and check initial name and age
# user1.name = 'Mark'   # rewrite
# user1.age = '80'      # rewrite
userHello = user1.say_hello(word = 'Hello')

print(user1.name)

### FUNCTION 'Dir' : returns the list from all attributes available inside the object
print(dir(user1))

### Define whether the object contains a particular attribute --> function 'hasattr'
res = hasattr(user1, 'name')
print(res)   # returns 'true'

### Assign the attribute to object externally (not inside the class) - CASE 1 (not recommended)
user1.new_attr = 'ABC'
res = hasattr(user1, 'new_attr')
print(res)    # recieving 'true'

### Assign the attribute to object externally (not inside the class) - CASE 2 (recommended)
setattr(user1, 'new_attr_plus', 'value')
res = hasattr(user1, 'new_attr_plus')
print(res)    # recieving 'true'

### Dynamically creating the attribute for the object using 'setattr'
attribute = 'new_attr_plus2'
setattr(user1, attribute, 'attribute_value')
print(hasattr(user1, 'new_attr_plus2'))

### Dynamically creating the attribute for the object using 'setattr'
attribute = 'new_attr_plus2'
setattr(user1, attribute, 'attribute_value')
print(hasattr(user1, 'new_attr_plus2'))

### Dynamically getting the attribute for the object using 'getattr' 
print(getattr(user1, 'new_attr_plus3', None))   ## !!! Attention -> we can use 'None' for case:
# when attribute is absent but we need to receive positive response, not error

### Delete the attribute for the object using 'delattr' 
print(dir(user1))   # has attribute = 'new_attr_plus2' in 'user1'
delattr(user1, attribute)
print(dir(user1))   # not available the attribute = 'new_attr_plus2' in 'user1'

### LET's look on INHERITANCE - create a class 'programmist' (inheritance)

class Programmer(AbstractUser):
    language = 'Python'    # let's remain only the difference between the classes

programmer1 = Programmer(initial_name='Mark', initial_age=50)
print(programmer1.say_hello('Hi'))
print(programmer1.language)
print(isinstance(programmer1, Programmer))
print(isinstance(programmer1, AbstractUser))
print(isinstance(user1, Programmer))


### REDEFINITION OF THE FUNCTION/METHOD INSIDE THE OBJECT (inheritance / polymorphism)

## Let's redefine the method 'say hello' by adding a new piece 'I will be ok in {age} years also':
class Programmer(AbstractUser):
    language = 'Python'    # let's remain only the difference between the classes
    def say_hello(self, word):
        return f'{word}, my name is {self.name} and I am {self.age} years. I will be ok in {self.age} years also'

programmer2 = Programmer(initial_name='Nick', initial_age=100)

print(programmer2.say_hello('Hi'))   # here we can see the redefined method 

# --> POLYMORPHISM, when object of different classes work in different way

print(programmer1.say_hello('Hi'))   # here we can see the initial method 

#   ""MULTIPLE INHERITANCE - object can inherit from different classes""
## !!! Inheritance is provided from the 'bottom' to the 'top' in the class hierarchy
# Example:
class A:     # --> branch x0
    a = 10

class B(A):  # --> branch x1
    a = 20

class C:     # --> branch y
#    a = 40
    pass

class D(C, B): # --> branch xy inherits from y and x1
    pass

d = D()
print(d.a)  # returns a = 40 --> search of 'a' is done in the most bottom branch whic contains 'a'
# if we comment the 'a' in 'class C', then print(d.a) = 20 --> search of 'a' is done in the most bottom branch whic contains 'a'
# if we comment the 'a' in 'class B(A)', then print(d.a) = 10 --> search of 'a' is done in the most bottom branch whic contains 'a'
# if we comment the 'a' in 'class A', then print(d.a) = Error --> search of 'a' is done in the most bottom branch whic contains 'a'

# Also we can check the order of the search using 'mro' method:
print(D.mro()) # from lef to the right: [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]



