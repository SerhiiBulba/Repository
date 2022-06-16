### ITERATOR

## simplest case is object 'for'
lst = [1, 2, 3]
for i in lst:
    pass

## In Python we have function 'iter'. It reverts any object into iterator.
iterator = iter(lst)
## Function 'next' returns the every next value from iterator - iterator can remind the current value and value to be returned as the next:

print(next(iterator))   # returns '1'
print(next(iterator))   # returns '2'
print(next(iterator))   # returns '3'
print(next(iterator))   # returns 'Error 'StopIteration'
