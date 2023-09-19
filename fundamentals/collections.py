motorcycles = ["honda", "yamaha" , "suzuki"]
print(motorcycles)

# Appending element into a list
motorcycles.append("ducati")
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)

removedItem = motorcycles.pop()
print(removedItem)
print(motorcycles)

removedItem_2 = motorcycles.pop(2)
print(removedItem_2)
print(motorcycles)

print("----------------------------------------------------------------")
removed_item_3 = 'ducati'
motorcycles.remove(removed_item_3) # was delete only the first occurrence
print(removed_item_3) # logic to work with item here
print(motorcycles)

print("\n2. Organizing a List --------------------------------")
print("\na. Sorting permanently--------------------------------")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print("\na. Sorting Temporarily with sorted() --------------------------------")
print("----Here is original list: ")
print(cars)
print("----Here is sorted list: ")
print(sorted(cars))
print("----Here is original list again: ")
print(cars)

print("\nc. Reverse order ------------------- ")
cars.reverse()
print(cars)



# Make a list of numbers
numbers = list(range(10))
print(numbers)

# Giving a step size when generating numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)


# Squares
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# ----------------------------------------------------------------

squares_2 = [value**2 for value in range(1, 11)]
print(squares_2)

# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:3])
print(players[2:])

print(players[-2:])

# Copy a List
print(players[:])


