### Function "Super"  --> we can call the parent class

class A:
    a = 0
    def __init__(self, new_a):
        self.a = new_a

class B(A):
    b = 10
    def __init__(self, new_a, new_b):
        super().__init__(new_a)  # --> function 'super' calls the parent class if it exists
        self.b = new_b

obj_b = B(100, 200)
print(obj_b.a)
print(obj_b.b)

### (!!!) Always need to define all the attributse related to the class:
# this is quite important for: 
# --> inheritance - if attribute is not in class A, but in method A, then attribute cannot be inherited in by descending object obg_B from class B
# --> clarity - if attribure is available in class, then it is more clear what attributes are included into the class

class A:   # Correct (+)
    a = 1
    b = 2
    def func(a, b):
        pass

class A:   # Incorrect (-)
    def func(a, b):
        a = 1
        b = 2
        pass

### (!!!) Class is the scheeme of object interpretting, and Object - is the output of the scheem run

### when we want to mark some attribute as private, we can use the 'underscore'
class Human:
    age = 10
    _phoneNumber = '025'     # we mark as protected (for use internally the method), but acces to attr is available outside the object
    __address = 'Lugova 15'   # we mark as Private, and acces to attr is NOT available outside the object
    def phone_message(self):
        return f'My pnone is {self._phoneNumber}'
    def address_message(self):
        return f'My pnone is {self.__address}'

phone = Human()
print(phone._phoneNumber)        # returm the attr via method - OK
print(phone.phone_message())     # returm the attr via method - OK
# print(phone.__address)            # returm the error 'Human' object has no attribute '__adress'
print(phone.address_message())   # returm the attr - OK

# But we can derive the private_attr from the object using: <obj_name>._<Class_name>.__<attr_name>
print(phone._Human__address)     # returm the attr - OK

### Magic method '__dict__'  - derives the attributes and their values assigned to the object
phone.age = 20
print(phone.__dict__)   # returns {'age': 20} -> where we can see the reassigned value to the attr 'age'

## If not using __init__, then attr is stored on the Class_level, not Object_level
## If using __init__, then attr is stored on the Object_level (can be redefined when initializing the object)


### TASK: I want to create object 'Point' and create descending objects in figures
#         And need to validate the input for coordinates - should be int/float

# Step 1: Create a class 'Point':

class Point:
    x = 0
    y = 0
    def __init__(self, x_coord, y_coord):
        if not isinstance(x_coord, (int, float)) or not isinstance(y_coord, (int, float)):
            raise TypeError
        self.x = x_coord
        self.y = y_coord


p1 = Point(5, 10)
