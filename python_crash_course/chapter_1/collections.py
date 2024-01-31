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

## delete element from the list
del bicycles[0]
print(bicycles)
assert len(bicycles) == 4, "Delete element failed"

## remove
print("remove element")
removed_ele = bicycles.pop() # or pop(-1) for index argument
assert removed_ele == 'suzuki', "Pop element failed"
assert len(bicycles) == 3, "Pop element failed"

print(bicycles)
bicycles.remove('readline')
assert len(bicycles) == 2, "Remove element failed"

# Insert element into list
bicycles.insert(0, 'specialized')
bicycles.insert(-1, removed_ele)
print(bicycles)

# Organize List
## ---- sort list permanently
print('------ before ---------')
print(bicycles)
bicycles.sort()
print('------ after ---------')
print(bicycles)

## ---- sort list temporarily
print('------ before ---------')
print(bicycles)
sorted_list = sorted(bicycles, reverse=True)
print('------ after ---------')
print(bicycles)
print(sorted_list)
print(bicycles == sorted_list)

## ---- reverse list:
print('------ before ---------')
print(bicycles)
bicycles.reverse()
print('------ after ---------')
print(bicycles)

# Working with list: loop

current_number = 0
while current_number < 5:
    print('------ current_number: ' + str(current_number))
    current_number += 1

