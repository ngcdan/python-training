# Reading Notes


## Working with List

- Loop over the list

```python
for item in list:
  pass
```

- Making Numerical Lists
```python
# start counting at first value (optional, default is 0), stop when reaches second value
for value in range(1, 5):
  print(value)
# 1
# 2
# 3
# 4

# making list of numbers
numbers = list(range(1, 6))
# [1, 2, 3, 4, 5]


# Using three arguments for step size
even_numbers = list(range(2, 11, 2))
# [2, 4, 6, ...]

```

- Statistics with a List of numbers
```python

numbers = list(range(1, 6))
min(numbers)
max(numbers)
sum(numbers)
```

- List comprehensions (create a new list from an existing one)
```python

# Create a new list from an existing one
squares = []
for value in range(1, 11):
  square = value**2
  squares.append(square)
print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)

# filter elements in a list
numbers = range(11) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [number for number in numbers if number % 2 == 0]

# Create a list from multiple list
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
combine_list = [(x, y) for x in list_1 for y in list_2]
# [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
```

## Working with part of a list

- Slice of list
```python
numbers = range(11)
sliced_numbers = numbers[0: 6] # [0, 1, 2, 3, 4, 5]
from_start_numbers = numbers[:6] # [0, 1, 2, 3, 4, 5]

to_end_numbers = numbers[4:] # [4, 5, 6, 7, 8, 9, 10]
to_end_numbers = numbers[-3:] # [8, 9, 10]

```

- Copy a List
```python
numbers = range(11)
copy_list = numbers[:]

```

## Working with Tuple (items can not change - _immutable_)
- _Tuple look like list, but use () instead of []_

```python
dimensions = (200, 50)
for dimension in dimensions:
  print(dimension)
```

## Working with Dict
_Collection of key - values pairs, a key's value can be a number, a string, a list or a dictionary_
_Note: As of Python 3.7, dict retain the order of insertion_

```python

alien = {'color': 'green', 'points': 5}

# Accessing values
color = alien['color'] # key does not exist, => error
# Usign get() method to set default value, if default value is not provided, then return None
color = alien.get('color', 'red')

```

- Loop over dict
```python
user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")


# Looping through all the keys in a dict
for key in user.keys():
    print(key) # username, first, last

# same behavior as above
for key in user:
    print(key)

# Looping through a key in a particular order
for key in sorted(user.keys()):
    pass

# Looping through all the values in a dict
for value in user.values():
    pass

# Looping through all the value nonrepetitive => using set to remove duplicates
for value in set(user.values()):
    pass
```

## User input
_The input() function pauses your program and waits for the user to enter something._

```python
name = input('Please enter your name!!') # => return always string value
print(f'Hello {name}')

# int() function convert string to int
age = input('Please enter your age!!') # => return always string value
int(age) > 18

```
_A for loop is affective for looping through a list, but shouldn't modify a list inside a for loop because will have trouble_
_keeping track of the items in the list_

_To modify a list as you work throught it, use a while loop_
_Case study: Remove all instances of specific values from a List_

# Working with function
## Passing an Arbitrary Number of Arguments
_Sometimes you won't know how many arguments a function needs to accepts._

```python
def make_pizza(*toppings):
  """The asterisk in the argument name *toppings tells Python to make an empty tuple called toppings
  and pack whatever values it receives into this tuple. Any number of toppings can be passed to make_pizza()
  """
  pass

make_pizza('peperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

```

- Example user_profile.py
```python
def build_profile(first, last, **user_info):
  """Buld a dict containing everything we know about a user"""
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# => {'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics'}
```

__Storing your functions in a seperate file allows you to hide the details of your program's code and focus on its higher-level logic__

# Working with File

*file_reader.py*
```python
# Open a file, python looks in the dir where the file that's currently being executed.
with open('file_name.txt') as file_object: # _with_ keyword automatically close the file
  contents = file_object.read()
print(contents)


# Can read files from any location on your system.
file_path = '/Users/username/Desktop/file_name.txt'
with open(file_path) as file_object:
  contents = file_object.read()
print(contents)

```

*file_writer.py*
```python
# Open a file
with open('programming.md', 'w') as file_object: # read mode (r) => default, write mode (w), append mode (a), read and write mode (r+)
  file_object.write("\nI love programming.")

```

*NOTE: Python can only write strings to a text file. sometimes you have to convert the data to string using the str() func*







