import json

file_name = 'programming.md'

# 'w' tells Python that we want to open the file in write mode, read mode ('r'), append mode ('a')
# with open(file_name, 'w') as file_object:
#     file_object.write("I love programming.")

# with open(file_name, 'a') as file_object:
#     file_object.write("\nI love programming")

numbers = [2, 3, 5, 7, 11, 13]
file_name_2 = 'numbers.json'
with open(file_name_2, 'w') as file_object:
    json.dump(numbers, file_object)
