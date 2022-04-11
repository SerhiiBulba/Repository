#Task: "Cinema BoxOffice"
#ShortDescription: As Visitor I want to have my age validated by the system So that control over ticker sales can be handled
#Details:
# Попросіть користувача ввести свсвій вік (можно використати константу або input()).
# - якщо користувачу менше 7 - вивести "Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Це фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Покажіть пенсійне посвідчення!"
# - якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "Який цікавий вік!"
# - у будь-якому іншому випадку - вивести "А білетів вже немає!"

print('Please, input your age:')
str_var = input()
a = int(str_var)
if a < 7:
    print('Where are your parents?')
elif a > 7 and a < 16:
    print('This film is for adults only! Sorry, cannot sell the tickets.')
elif a > 65 and a % 11 != 0:
    print('Please, show your pension certificate')
elif a > 16 and a % 11 == 0:
    print ('What an amazing age!')
else:
    print('Sorry, no tickets available')

# Consern: based on the task description there is no tickets availability for the adults of the age 16-65