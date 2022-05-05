# def year_append(age):
#     x = str(age)
#     if int(x[-1]) == 1:
#         print('рік')

age = input('Please, input the age: ')
def year_append(age):
    lst1 = ['1']            # для додавання: "рік"
    lst2 = ['2', '3', '4']      # для додавання: "роки"
    lst3 = ['0', '5', '6', '7', '8', '9']      # для додавання: "років"
    age_str = str(age)
    if age_str[-1] in lst1:   # додавання "рік", якщо age закінчується на '1'
        print('рік')
    if age_str[-1] in lst2:   # додавання "роки", якщо age закінчується на '2', '3', '4'
        print('роки')
    if age_str[-1] in lst3:   # додавання "років", якщо age закінчується на '0', '5', '6', '7', '8', '9'
        print('років')

text = year_append(age)


print('strin1 {}'.format(text))


## Section 2: Input the text appends:
def year_append(age):
    lst1 = ['1']                           # для додавання: "рік"
    lst2 = ['2', '3', '4']                 # для додавання: "роки"
    lst3 = ['0', '5', '6', '7', '8', '9']  # для додавання: "років"
    age_str = str(age)
    if age_str[-1] in lst1:                # додавання "рік", якщо age закінчується на '1'
        print('рік')
    if age_str[-1] in lst2:                # додавання "роки", якщо age закінчується на '2', '3', '4'
        print('роки')
    if age_str[-1] in lst3:                # додавання "років", якщо age закінчується на '0', '5', '6', '7', '8', '9'
        print('років')