# def foo(a):
#     print(a)

# foo('Hi')


# def hello(a, b):
#     print(a + b)

# foo('Hi')
# hello('hello', 'Gym')

# print(__name__)

new_x = '10'
#print(isinstance(new_x, (int, float)))
try:
    type(new_x) is int
except:
    print('error')
else:
    print('true')  