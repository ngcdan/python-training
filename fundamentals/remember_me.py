import json
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
file_name = 'username.json'

try:
    with open(file_name, 'r') as file:
        username = json.load(file)
except:
    username = input('What is your username?\n')
    with open(file_name, 'w') as file:
        json.dump(username, file)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username} ")