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