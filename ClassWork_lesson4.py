# Teacher suggest us use the cycle "for" for working under collections (list, tuple)
for element in (1, 2, 3):
    print(element)

## Data Type "dictionary"
my_dict = {0: 'a', 1000.1: 'b', 100: 'c'}
print(my_dict)
print(my_dict[0])
print(my_dict[1000.1])


# search the data in list is provided through the 'index', but in dictionary - by the 'key'
# the data: 0, 100.1 and 100 are the 'key' of the dictionary

# what data types could be the keys to ductionary? They are: int, float, string, bool, tuple and None
# By the way  - fata type of key is always static data
my_dict = {
    0: 'a',
    1000.1: 'b',
    'string': 'c',
    True: '1500',
    (1, 2): '125fgds',
    None: '45ff',
    'Dictionary': {1: 'gfd'}
    }

print(my_dict)
print(my_dict['Dictionary'])

# If I want to add the new key with value into dictionary:
my_dict['name'] = 'new strint'
print(my_dict)

# If need to rewrite the value, I need to push the request with the same key but with different value:
my_dict['name'] = ['fd', 1, [1, 2]]
print(my_dict)

# I can derive the data from the list, which is included into the dictionary:
print(my_dict['name'])
print(my_dict['name'][0])
# so based on the above mentioned: all operations with lists and strings are available inside the dectionary

## We can use the cycle 'For' for dictionary:
for i in my_dict:
    print(i)
# we received the key - so, to retreive the keys fron the dictionary we can use the cycle "for"

my_dict = {
    0: 'a',
    1000.1: 'b',
    'string': 'c',
    True: '1500',
    (1, 2): '125fgds',
    None: '45ff',
    'Dictionary': {1: 'gfd'}
    }
# How we can retrive the values fron the dictionary? There are several approaches:

#Approach 1:
for i in my_dict:
    print(my_dict[i])

#Approach 2: we can use methods 'key' and 'value' for the dictionary
for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for item in my_dict.items():
    print(item)

for key, value in my_dict.items():
    print(key)
    print(value)

### Working with dynamic and static data
# Sample of dynamic data - there are changes when cut data from a particular chunk of memory and store it in another
var1 = 1
print(id(var1))  # whithin a peace of program the chunk is '1433771704560'
var1 += 1
print(id(var1))  # if make calculation then chunk is '1294123663632', so it is dynamic from operation to operation


# Sample of static data - No changes when cut data from a particular chunk of memory and store it in another
list1 = [1, 2]
print(id(list1))   # whithin a peace of program the chunk is '2805489587136'
list1.append([2, 3])
print(id(list1))   # if make calculation then chunk is still '2805489587136', so it is static from operation to operation

# another sample with string
my_str = 'fda'
print(id(my_str))
my_str.replace('f', 'N')
print(id(my_str))
#** The key in the dictionary could be only static data

### How to remove the 'key' with 'value' from the dictionary:
my_dict = {
    True: 'a',
    1000.1: 'b',
    'string': 'c'
        }

my_dict.pop(True)
print(my_dict)

## How to add the 'key' with 'value' from the dictionary:
my_dict['new key'] = 'new value'
print(my_dict)


### How to update the 'key' with 'value' from the dictionary (in this case the key/value is updated unlikely to the case above):
my_dict.update({'new key': 'new value'})
print(my_dict)
my_dict.update({'new key': '1'})
print(my_dict)

print(my_dict)

## ! We cannot multiply the dictionary by some value (dict * value) !

### SET data type
# set contains only unick data
# there is not any order in data set, no priorities, no indexes and no keys
# we can add data to set but whithout any order. We can remove data
# Set can be used for analytic mathematics. Also we can infiltrate the uniq values through the set
my_set = {2, 1, 3, 5, 'a'}
my_set.add('f')
print(my_set)
my_set.remove('a')
print(my_set)


## How to ask if the particular element exists in the dictionary, set?
print('a' in my_dict.values())  # receiving the True
print('f' in my_set)            # receiving the True
print('a' in my_set)            # receiving the False  - because, the 'a' was removed during the code in row 131

### FROZEN SET data type
# this data type is similar to Set. But for creating the set need the function
frozen_set = frozenset([1, 2, 3])
print(frozen_set)

## How to get data from dictionary - use method  'GET'
# dictionary_name_get('a', 'b'), where 'a' - key, 'b' - default value returned if the key not found
my_dict = {
    True: 'a',
    1000.1: 'b',
    'string': 'c'
        }
print(my_dict.get(True, 'default data'))

### !!! Do not use <if 'a' or 'b' in lst>, but use <if ('a' in lst) or ('b' in lst)>
## for the case <if 'a' or 'b' in lst> the programm processes only the 1st element, which returns True.
## if none element is with True, then the programm processes the latest element, which returns False
## unlike the "OR", operator "AND" processes only the 1st element, which returns False

### False case is equal to: 1) 0 or 0.000; 2) empty string, list, tuple, dictionary, set; 3) None
##  True case is when: 1) at least any value exists except 0 or 0.00; 2) True

### TERNARY operator if-else
## Python Ternary operator is used to select one of the two values based on a condition. \ 
# It is a miniature of if-else statement that assigns one of the two values to a variable.
## for instance: return 'Hello' if condition is True, and return 'Buy' if condition is False
condition = True
res = 'Hello' if condition else 'By'
print(res)

### IF need to create a list with a range from 0 to 10, we can use the operator "for"
## Approach 1: using standart cycle 'for'
lst = []
for i in range(11):
    lst.append(i)
print(lst)

## Approach 2: usin 'comprehension'
lst = [i for i in range(11)]
print(lst)

### If need to derive a list with a range of squared numbers (0^2, 1^2, 2^2 ..., 10^2)
lst = [i ** 2 for i in range(11)]
print(lst)

### If need to derive a list of strings including the squared numbers in range 0...10 ('0^2', '1^2', '2^2' ..., '10^2')
lst = [str(i ** 2) for i in range(11)]
print(lst)

### If need to convert the string '1234567' into a list of strings including the squared numbers in range 0...10 ('0^2', '1^2', '2^2' ..., '10^2')
lst = [str(int(i) ** 2) for i in '1234567']
print(lst)

### create a list from the elements of range 0...10 with the next condition: for pair element need to square, for odd elements - need to cube.
## Approach 1: use 'for'
lst = []
for i in range(11):
    if not i % 2:
        elem = i ** 2
    else:
        elem = i ** 3
    lst.append(elem)

print(lst)

## Approach 2: use 'comprehension'
lst = [int(str(i ** 2)) if not i % 2 else int(str(i ** 3)) for i in range(11)]
print(lst)

## Approach 3:
lst=[str(i ** 2) for i in range(11) if i % 2]
print(lst)

### Comprehansion for dictionary: create the dictionary where for every key its value is key^2
## Approach 1:
my_dict = {}
for i in range(11):
    my_dict[str(i)] = i ** 2

print(my_dict)

## Approach 2:
my_dict = {str(i): i ** 2 for i in range(11)}
print(my_dict)


### How to create the SET using ternary operator:
my_set = {i for i in range(11)}
print(my_set)

### How to create the GENERATOR using ternary:
my_tuple = (i for i in range(11))
print(my_tuple)