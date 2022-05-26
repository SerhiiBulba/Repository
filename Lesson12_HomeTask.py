### Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від "Транспортний засіб". \
#  Наповніть класи атрибутами на свій розсуд. Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

# ACCEPTANCE CRITERIA:
# 1 --> class 'Vehicle'
# 2 --> subclasses 'Car', 'Plane', 'Sheep' from the class 'Vehicle'
# 3 --> attributes are created for each object, Atrributes could be Any.
# 4 --> objects for each subclass('Car', 'Plane', 'Sheep')

# Code:

class Vehicle:
    """Parent class 
    """    
    vehicle_speed = {'CAR': 50, 'PLANE': 600, 'SHIP': 25}   # variants of speed for different types of vehicles
    vehicle_color = {'CAR': 'red, black', 'PLANE': 'white', 'SHIP': 'white'}     # variants of colors
    def Vehicle_Info(vehicle_speed, vehicle_color):
        """Returns the infor regarding Vehicle

        Args:
            vehicle_speed (dict): speed range
            vehicle_color (dict): color range
        """        
        model = input(f'please, input the model: ')
        return(f'Vehicle model is {model}. Speed is {vehicle_speed} km/h.  Color is {vehicle_color}.')      

## **** Creating the subclass 'Car' from the parent class 'Vehicle'****
class Car(Vehicle):
    """Child Class from 'Vehicle'

    Args:
        Vehicle (class): parent class
    """
    def car_info(type_car):
        info = f'Car type is {type_car}. '
        return info

# Created the object based on class 'Car':
Car_object = Car

# Retrieve the information related to the 'Car'
type_info = Car_object.car_info(type_car = input(f'please, input the type: '))
parameter_info = Car.Vehicle_Info(vehicle_speed = Vehicle.vehicle_speed.get('CAR'), vehicle_color = Vehicle.vehicle_color.get('CAR'))
print(type_info + parameter_info)


## *****  Creating the subclass 'Plane' from the parent class 'Vehicle' *****
class Plane(Vehicle):
    """Child Class from 'Vehicle'

    Args:
        Vehicle (class): parent class
    """
    def plane_info(type_plane):
        info = f'Plane type is {type_plane}. '
        return info

# Created the object based on class 'Plane':
Plane_object = Plane

# Retrieve the information related to the 'Plane'
type_info = Plane_object.plane_info(type_plane = input(f'please, input the type: '))
parameter_info = Plane.Vehicle_Info(vehicle_speed = Vehicle.vehicle_speed.get('PLANE'), vehicle_color = Vehicle.vehicle_color.get('PLANE'))
print(type_info + parameter_info)

## *****  Creating the subclass 'Ship' from the parent class 'Vehicle' *****
class Ship(Vehicle):
    """Child Class from 'Vehicle'

    Args:
        Vehicle (class): parent class
    """
    def ship_info(type_ship):
        info = f'Ship type is {type_ship}. '
        return info

# Created the object based on class 'Ship':
Ship_object = Ship

# Retrieve the information related to the 'Ship'
type_info = Ship_object.ship_info(type_ship = input(f'please, input the type: '))
parameter_info = Ship.Vehicle_Info(vehicle_speed = Vehicle.vehicle_speed.get('SHIP'), vehicle_color = Vehicle.vehicle_color.get('SHIP'))
print(type_info + parameter_info)




