current_number = 1
while current_number < 4:
    print(current_number)
    current_number += 1


# Remove all instances of the specific values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Filling a dictionary with user input
responses = {}

# Set a flag to indicate that polling is active
polling_action = True
while polling_action:
# Prompt for the person's name and response
    name = input("What your name? \n")
    mountain = input("Which mountain would you like to climb someday\n")

    # Store the response in a dictionary
    responses[name] = mountain

    # Find out if anyone else is going to take the polling
    repeat = input("Would you like to let another person respond? (yes/ no)\n")
    if repeat == 'no':
        polling_action = False


print("----------Result -----------------")
for name, mountain in responses.items():
    print(f"{name} would like to climb {mountain}")



