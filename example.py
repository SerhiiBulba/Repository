# age = input('Please, input the age: ')
# lst1 = ['1']                           # для додавання: "рік"
# lst2 = ['2', '3', '4']                 # для додавання: "роки"
# lst3 = ['0', '5', '6', '7', '8', '9']  # для додавання: "років"
# lst4 = ['11', '12', '13', '14', '15', '16', '17', '18', '19']   # для додавання: "років"
# age_str = str(age)
# if age_str in lst4:
#     text = 'років'
# else:
#     if (age_str[-1] in lst1):                # додавання "рік", якщо age закінчується на '1'
#         text = 'рік'
#     elif (age_str[-1] in lst2) and (age_str[-2] not in lst4):                # додавання "роки", якщо age закінчується на '2', '3', '4'
#         text = 'роки'
#     elif (age_str[-1] in lst3) and (age_str[-2] not in lst4):                # додавання "років", якщо age закінчується на '0', '5', '6', '7', '8', '9'
#         text = 'років'

# print(text)

# age = input('Please, input the age: ')
# def year_append(age):
#     lst1 = ['1']            # для додавання: "рік"
#     lst2 = ['2', '3', '4']      # для додавання: "роки"
#     lst3 = ['0', '5', '6', '7', '8', '9']      # для додавання: "років"
#     age_str = str(age)
#     if age_str[-1] in lst1:   # додавання "рік", якщо age закінчується на '1'
#         print('рік')
#     if age_str[-1] in lst2:   # додавання "роки", якщо age закінчується на '2', '3', '4'
#         print('роки')
#     if age_str[-1] in lst3:   # додавання "років", якщо age закінчується на '0', '5', '6', '7', '8', '9'
#         print('років')

# text = year_append(age)


# print('strin1 {}'.format(text))


# ## Section 2: Input the text appends:
# def year_append(age):
#     lst1 = ['1']                           # для додавання: "рік"
#     lst2 = ['2', '3', '4']                 # для додавання: "роки"
#     lst3 = ['0', '5', '6', '7', '8', '9']  # для додавання: "років"
#     age_str = str(age)
#     if age_str[-1] in lst1:                # додавання "рік", якщо age закінчується на '1'
#         print('рік')
#     if age_str[-1] in lst2:                # додавання "роки", якщо age закінчується на '2', '3', '4'
#         print('роки')
#     if age_str[-1] in lst3:                # додавання "років", якщо age закінчується на '0', '5', '6', '7', '8', '9'
#         print('років')

### PROGRAM CODE : ###

list = [11, 22, 33, 44, 55, 66, 77, 88, 99]

"""_Section 1: Input the list (global data) with values of awesome age:_
"""
# Check the input using the cycle
def validate():
    while True:
        try:
            age = input(f'Please, input the age:')
            age_int = int(age)
        except:
            print('Should be integer only, not float, not empty')
        else:
            if age_int > 0:
                break
            else:
                print(f'should be > 0')
    return age

age = int(validate())

"""_Section 2: Input the text appends (global data):_
"""
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

def check_match(age):
    """_Section 3: FUNCTION "check if the age contains the matched digits (11, 22 ...)_
    Args:
        age (_str_): _age of the Customer_
    """    
    if age in list:
        print('О, вам {} {}! Який цікавий вік!'.format(age, text))

    
def return_response(age):
    """_Section 4: FUNCTION "Return response":_
    Args:
        age (_str_): _age of the Customer_
    """    
    if check_match(age) is True:
        check_match(age)
    elif age < 7:
        print('Тобі ж {} {}! Де твої батьки?'.format(age, text))
    elif (age >= 7) and (age < 16) and (age not in list):
        print('Тобі лише {} {}, а це е фільм для дорослих!'.format(age, text))
    elif (age >= 16) and (age < 65) and (age not in list):  
        print('Незважаючи на те, що вам {} {}, білетів всеодно нема!'.format(age, text))
    elif (age >= 65) and (age not in list):  
        print('Вам {} {}. Покажіть пенсійне посвідчення!'.format(age, text))
    
return_response(age)


def Car_Info(model, car_speed, car_weight):
        """Returns the infor regarding Vehicle

        Args:
            car_speed (dict): variants of speed for different types of vehicles
            car_weight (list): weight range
        """        
    car_speed = 50
    car_weight = '1250 - 2100 kg'
    model = input(f'please, input the name: ')
    return(f'Vehicle model is {model}. Speed is {car_speed} km/h.  Weight is {car_weight}.')