#Task: "Cinema BoxOffice"
#ShortDescription: As Visitor I want to have my age validated by the system So that control over ticker sales can be handled
#Details:
# Попросіть користувача ввести свсвій вік (можно використати константу або input()).
# - якщо користувачу менше 7 - вивести "Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Це фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Покажіть пенсійне посвідчення!"
# - якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "Який цікавий вік!"
# - у будь-якому іншому випадку - вивести "А білетів вже немає!"

# from mailbox import mbox, mboxMessage
# from tkinter import messagebox
# from tkinter.messagebox import showinfo
# import turtle
# sc = turtle.Screen()
# sc.setup(500, 300)
# str_var = turtle.textinput('TicketBox', 'Please, input your age')
# age = int(str_var)
# if age < 7:
#     messagebox.showinfo('Box info','Where are your parents ?')
# elif age > 7 and age < 16:
#     messagebox.showinfo('Box info','This film is for adults only! Sorry, cannot sell the tickets ?')
# elif age > 65 and age % 11 != 0:
#     messagebox.showinfo('Box info', 'Please, show your pension certificate?')
# elif age > 16 and age % 11 == 0:
#     messagebox.showinfo('Box info', 'What an amazing age!')
# else:
#     messagebox.showinfo('Box info', 'Sorry, no tickets available')

# Consern: based on the task description there is no tickets availability for the adults of the age 16-65


# Inputs validation check:


age = input('Input: ')

# check if input is empty
if len(age) == 0:
    print('no data inputted')
# check if input contains letters   
elif age.isalnum() == True:
    print('contains letter')
# check if input is less or equal to zero0
elif int(age) < 0:
    print('age could not be less than zero')
elif int(age) == 0:
    print('age could not be equal to zero')



    