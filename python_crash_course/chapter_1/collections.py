# List
bicycles = ['trek', 'cannondale', 'readline', 'specialized']
print(bicycles)

## Print last element of the list
print(bicycles[-1])

## Modify
bicycles[0] = 'honda'
print(bicycles)

## add element to the list
bicycles.append('suzuki')
print(bicycles)

motorcycles = []
motorcycles.extend(['honda', 'cannondale', 'readline', 'specialized'])
print(motorcycles)

## delete element from the list
del bicycles[0]
print(bicycles)
assert len(bicycles) == 5, "Delete element failed"

## remove
bicycles.pop()