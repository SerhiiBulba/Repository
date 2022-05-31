## Дякую, що зачекали :)

## Task 1: Доопрацюйте класс Point так, щоб в атрибути х та у обʼєктів цього класу можна було записати тільки числа. 
# Використовуйте property

## For the validation rule I used 'if-else' instead 'if-raise', -> this is for returning the reason of the error happened

##-----Class Point-----
class Point:
    """Point class defines the cooridnates of a single point

    Returns:
        _type_: _description_
    """
    _x = None
    _y = None
    error_key = 'TypeError for:'
    error_message = 'Message: Only int/float allowed for the argument'

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, new_x):
        if not isinstance(new_x, (int, float)):
            print(Point.error_key, 'argument X','|', Point.error_message)          
        else:
            self._x = new_x
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, new_y):
        if not isinstance(new_y, (int, float)):
            print(Point.error_key, 'argument Y','|', Point.error_message)          
        else:
            self._y = new_y

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

# simple unit test for the point class:
# point1 = Point(1, '1')
# print(point1.x)
# print(point1.y)

# Task 2:  Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point).  
# Реалізуйте перевірку даних, що пишуться в точки аналогічно до класу Line. Визначет атрибут,  
# що містить площу трикутника (за допомогою property). Для обчислень можна використати формулу Герона



 ##-----Class Triangle-----


class Triangle:
    """Defines the corners of the Triangle ABC and calculates its square using coordinates over the points A, B and C

    Raises:
        TypeError: ErrorType for corner1 (point A) (only int/float are allowed)
        TypeError: ErrorType for corner2 (point B) (only int/float are allowed)
        TypeError: ErrorType for corner3 (point C) (only int/float are allowed)

    Returns:
        float: square of the Triangle
    """    
    # set the attributes for the corners of the Triangle
    _corner1 = None
    _corner2 = None
    _corner3 = None
    
    # initiate the corner points of the Triangle:
    def __init__(self, apex1, apex2, apex3):
        self.corner1 = apex1
        self.corner2 = apex2
        self.corner3 = apex3

    # define 'read' property for corner1:
    @property
    def corner1(self):
        return self._corner1

    # define 'setup' property for corner1:
    @corner1.setter
    def corner1(self, new_corner1):
        if not isinstance(new_corner1, Point):
            raise TypeError
        self._corner1 = new_corner1      

    # define 'read' property for corner2:
    @property
    def corner2(self):
        return self._corner2

    # define 'setup' property for corner2:
    @corner2.setter
    def corner2(self, new_corner2):
        if not isinstance(new_corner2, Point):
            raise TypeError
        self._corner2 = new_corner2   

    # define 'read' property for corner3:
    @property
    def corner3(self):
        return self._corner3

    # define 'setup' property for corner3:
    @corner3.setter
    def corner3(self, new_corner3):
        if not isinstance(new_corner3, Point):
            raise TypeError
        self._corner3 = new_corner3

    # -> define property for Squeare of Triangle ABC:
    @property
    def square_abc(self):

        # calculate the legth of the side AB:
        lab_x = (self._corner1.x - self._corner2.x) ** 2
        lab_y = (self._corner1.y - self._corner2.y) ** 2
        length_ab = (lab_x + lab_y) ** 0.5

        # calculate the legth of the side AC:
        lac_x = (self._corner1.x - self._corner3.x) ** 2
        lac_y = (self._corner1.y - self._corner3.y) ** 2
        length_ac = (lac_x + lac_y) ** 0.5        

        # calculate the legth of the side BC:
        lbc_x = (self._corner2.x - self._corner3.x) ** 2
        lbc_y = (self._corner2.y - self._corner3.y) ** 2
        length_bc = (lbc_x + lbc_y) ** 0.5        
        
        # calculate the half of Perimeter:
        p = (length_ab + length_ac + length_bc) / 2

        # calculate the square of the Triangle ABC:
        square_abc = (p * (p - length_ab) * (p - length_ac) * (p - length_bc)) ** 0.5
        
        return square_abc

# simple unit tests:
point1 = Point(1, 10)
point2 = Point(10, 25)
point3 = Point(7, 36)

triangle = Triangle(point1, point2, point3)
# triangle.corner1 = '1'  #-> should return the 'raise TypeError'
# triangle.corner2 = '2'  #-> should return the 'raise TypeError'
# triangle.corner3 = Point(1, 2)

print(triangle.square_abc)  #-> should return the square calculated over the  Point(1, 2)