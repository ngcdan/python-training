## Data Type Conversion Funcs

```python

amount = int(10.6);
# 10

amount = float(10); # 10.0

```

## String concatenation

```python

hello = "Hello"

```

## Pyt


## Working with list in python
- add item into list
```
acronyms = []
acronyms.append('LOL')
acronyms.append('IDK')
```

- remove item from list
```
acronyms.remove('IDK')
del acronyms[1]
```

- Check if exists in list
```
if 1 in [1, 2, 3, 4, 5]:
    print('True')


acronyms = ['LOL', 'IDK', 'SMH', 'TBH']
word = 'BFN'
if word in acronyms:
    print(word + " is in the list ")
else:
    print(word + " is NOT in the list ")
```

- Loop over each item in a list
```
acronyms = ['LOL', 'IDK', 'SMH', 'TBH']
for acronym in actonyms:
    print(acronym)
```

- Loop with range(start, stop, step)
```
for i in range(7):
    print(i)

```

## Working with dict
```
acronyms = {'LOL': 'laugh out loud' 'IDK': 'I don't know', }
definition = acronyms['BTW'] # Trying to access a key that doesn't exist will cause an error (KeyError: 'BTW')
definition = acronyms.get('BTW') # Using get() wont crash your program with an error, instead just return None

```
- Using a Dict' Key and Value in a for loop

```
for key, value in dict.items():
    print(key, ':', value)
```

## Catch Exceptions with a try/except block
```
try:
    definition = acronyms['BTW']
except KeyError:
    print('KeyError')


def remainder_exception(a, b):
    if b == 0:
        raise Exception('Divisor cannot be 0')
    else:
        return a % b

```

## Open a File in Python
```
# open() returns a File object that has methods like read() and write()
# It's important to close the file when you're done with it
file = open('data.txt')

# The with keyword makes file.close() automatic
with open('data.txt') as file:

    # read() method returns the whole file as a string, Or it will be return specified number of bytes
    print(file.read())

    # readline() method returns the next line of the file
    print(file.readline())

    # readlines() method returns the next lines of the file
    result = file.readlines()
    for line in result:
        print(line)
    for line in file:
        print(line)

try:
    # Do file operations here
    pass
finally:
    file.close()
```

- Check if string is a substring of a string
```
    if look_up in line:
        print(line)
```

## Builin lib functions working with File

### Working with file in os system
```
import os

# os.getcwd() returns the current working directory
os.getcwd()

ok.mkdir('/Users/linuss/Documents/Python')

# os.scandir() returns a list of files and directories
os.scandir(folder)
```
