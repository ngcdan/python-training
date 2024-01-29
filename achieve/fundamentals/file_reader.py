with open('../files_to_read/names.csv') as file_obj:
    content = file_obj.read()
    print(content)

# Read line by line
print("\n# Read line by line")
with open('../files_to_read/names.csv') as file_obj:
    for content in file_obj:
        print(content)

# Making a List of lines from File
print("\n# Making a List of lines from File")
with open('../files_to_read/names.csv') as file_obj:
    lines = file_obj.readlines()

for line in lines:
    print(line)

"""
When Python reads from a text file, it interprets all text in the file as a string.
If you read in a number and want to work with that value in a numerical context,
you’ll have to convert it to an integer using the int() function or convert it to a float using the float() function
"""
