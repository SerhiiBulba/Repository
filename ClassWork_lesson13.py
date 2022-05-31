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

# Step 1: Create class 'Point':

class Point:
    x = 0
    y = 0
    def __init__(self, x_coord, y_coord):
        if not isinstance(x_coord, (int, float)) or not isinstance(y_coord, (int, float)):
            raise TypeError
        self.x = x_coord
        self.y = y_coord

# Step 2: create point objects
p1 = Point(1, 2)
p2 = Point(4, 5)

# Step 3: create class "Line"
class Line: # (AGGREGATION)
    begin = None
    end = None
    def __init__(self, begin_point, end_point):
        # check wether begin_point, end_point belongs to class "Point":
        # here we use inheritance the validation rule from the class "Point"
        if not isinstance(begin_point, Point) or not isinstance(end_point, Point):
            raise TypeError 
        self.begin = begin_point
        self.end = end_point

line_1 = Line(p1, p2)  # here we use association -> when some object is used as attr for another one
# above object "p1" is used as attr for object "line_1" 

### ASSOCIATION can have 2 types:
## ---> AGGREGATION: approach when internal object (used fo assoc) can exists outside the class / object. "line_1" - is a sample of aggreg
#       in aggregation objects "p1" and "p2" exsist independently from the object "line_1"
## ---> COMPOSITION: approach when we bring data into the object for creating another objects inside the class. Sample below; 
class Line:  # (COMPOSITION)
    begin = None
    end = None
    def __init__(self, begin_point_x, begin_point_y, end_point_x, end_point_y):
        self.begin = Point(begin_point_x, end_point_x)
        self.end = Point(begin_point_y, end_point_y)
line_2 = Line(1, 2, 4, 5)    # we create the line not using ready points, but using the materials for creating the points - that's composition

# Step 4: to the class "Line" add the method to calculate the length between the points
class Line: # (AGGREGATION)
    begin = None
    end = None
    
    def __init__(self, begin_point, end_point):
        if not isinstance(begin_point, Point) or not isinstance(end_point, Point):
            raise TypeError 
        self.begin = begin_point
        self.end = end_point
    # define the distance between the points
    def get_distance(self):
        k1 = (self.begin.x - self.end.x) ** 2
        k2 = (self.begin.y - self.end.y) ** 2
        res = (k1 + k2) ** 0.5
        return res

p1 = Point(0, 5)
p2 = Point(0, 0)
line_3 = Line(p1, p2)
print(line_3.get_distance())

### CALCULABLE ATTRIBUTES --> we can assign the length to the line not calling the function "get_distance"
### Functionality which provides this ability is called "PROPERTY"
# Property - is a buildin function which provides ability to 'read', 'write' or/and 'delete' data

# Example:

# Usual case with function inisde class:
class Example1:
    val1 = 1
    val2 = 4
    # val3 = val1 + val2
    def sum(self):
        return self.val1 + self.val2
e = Example1()
print(e.sum())  # result = 5

### Case with "PROPERTY" function:
#  - property function allows to create the calculable attribute
# there are 2 ways:
# 
# # OBSOLETE APPROACH TO create 'PROPERTY' 

class Example2:
    val1 = 1
    val2 = 4
    # val3 = val1 + val2
    def value(self):
        return self.val1 + self.val2
    ## Poperty function:

    # 1 -> Reading the value:
    def value_getter(self):
        print(f'function for reading is run --->')
        return self.val1 + self.val2

    # 2 -> Writing the value:
    def value_setter(self, new_val):
        print(f'New value is set up ---> {new_val}')
        
    # 3 -> Deleting the value:
    def value_deleter(self):
        print(f'New value is deleted')
    
    #4 -> property function
    val3 = property(value_getter, value_setter, value_deleter)


e = Example2()

#let's read the data:
print(e.val3)  # result is "5"

#let's set up the data:
e.val3 = 1 # new value is added

#let's delete the 'val3' attribute from the object 'e':
delattr(e, 'val3')

# # MODERN APPROACH TO create 'PROPERTY' using "Decorator" 

class Example3:
    val1 = 10
    val2 = 10
    # define the property as decorator of inbuild function:
    
    # 1 -> Getter for reading
    @property 
    def value(self):
        print(f'function for reading is run --->')
        return self.val1 + self.val2
    
    # 2 -> Writing the value:
    @value.setter
    def value(self, new_val):
        print(f'New value is set up ---> {new_val}')
        
    # 3 -> Deleting the value:
    @value.deleter
    def value(self):
        print(f'New value is deleted')
    
e_n = Example3()

#let's read the data:
print(e_n.value)  # result is "5"

#let's set up the data:
e_n.value = 20 # new value is added

#let's delete the 'val3' attribute from the object 'e':
delattr(e_n, 'value')

### USE THE "PROPERTY" for 'get_distance' in the class 'Line' as virtual attribute

class Point:
    x = 0
    y = 0
    def __init__(self, x_coord, y_coord):
        if not isinstance(x_coord, (int, float)) or not isinstance(y_coord, (int, float)):
            raise TypeError
        self.x = x_coord
        self.y = y_coord

class Line: # (addin property inside)
    begin = None
    end = None
    
    def __init__(self, begin_point, end_point):
        if not isinstance(begin_point, Point) or not isinstance(end_point, Point):
            raise TypeError 
        self.begin = begin_point
        self.end = end_point

    # !!! -> define property for distance:
    @property
    def get_distance(self):
        k1 = (self.begin.x - self.end.x) ** 2
        k2 = (self.begin.y - self.end.y) ** 2
        res = (k1 + k2) ** 0.5
        return res

p1 = Point(0, 5)
p2 = Point(0, 0)
line_3 = Line(p1, p2)
print(line_3.get_distance)  # here we can call this property in the object "line_3"
                            # this means that everytime when we call the property, the function "get_distance" is run


#### LIVE CASE:
# We have classes Point and Line. When create an object for Line, we can try to set up string value for 'begin' or 'end'.
# In this case we receive Type error, because we're trying to call Line class not using the Point class (this class are separated). 
# Only 'Point' class has validation, so without using Point class we're not protected from errors.
# Lets replicate the case -> try to store for 'begin' the string value 'abc':
line_3.begin = 'abc'
print(line_3.get_distance)   # error: 'str' object has no attribute 'x'

# How we can to override the case: -> we can use the property function:
##-----Class Point----
class Point:
    x = 0
    y = 0
    def __init__(self, x_coord, y_coord):
        if not isinstance(x_coord, (int, float)) or not isinstance(y_coord, (int, float)):
            raise TypeError
        self.x = x_coord
        self.y = y_coord
##-----Class Line----
class Line:
    # make the protected variables:
    _begin = None
    _end = None

    # initiate the start-end points:   
    def __init__(self, begin_p, end_p):
        self._begin = begin_p
        self._end = end_p

    # define read property for begin:   
    @property
    def begin(self):
        return self._begin
    # define setup property for begin:  
    @begin.setter
    def begin(self, new_begin_p):
        if not isinstance(new_begin_p, Point):
            raise TypeError
        self._begin = new_begin_p
    # define read property for end:
    @property
    def end(self):
        return self._end     
    # define setup property for end:
    @end.setter
    def end(self, new_end_p):
        if not isinstance(new_end_p, Point):
            raise TypeError
        self.end = new_end_p
    # -> define property for distance:
    @property
    def get_distance(self):
        k1 = (self.begin.x - self.end.x) ** 2
        k2 = (self.begin.y - self.end.y) ** 2
        res = (k1 + k2) ** 0.5
        return res

point1 = Point(1, 2)
point2 = Point(10, 30)
line_obj = Line(point1, point2)

# --> rewriting the values for point1 and point2
line_obj._begin  = Point(0, 5)
line_obj._end  = Point(100, 150)

print(line_obj.get_distance)             

### Take aways from the approach:
# -> using pritected we are mitigated from the risk of rewriting the attributes
# -> using property provides ability to work with function outside as well as inside
# -> in this particular case when try to call with invalid (str) data, we can return the TypeError
# -> in real projects we can use property for extractiong some data from DB and them exploring this data in the code