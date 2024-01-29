import json

numbers = [2, 3, 4, 5, 6]
file_name = 'numbers.json'
with open(file_name, 'w') as file_object:
    json.dump(numbers, file_object)