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















