user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")

# Looping through all the keys in a dict
for key in user_0.keys():
    pass

## Another way, looping through the keys is actually the default behavior when looping a dict
for key in user_0:
    pass
# Looping in a particular order
for key in sorted(user_0.keys()):
    print(f"{key.title()}, thank you for taking the poll")

# Looping through all values in a dict: dict.values()
for value in user_0.values():
    print(f"{value}")

# Looping through all value nonrepetitive
for value in set(user_0.values()):
    print(f"{value.title()}")

# Build a set directly using braces, no key - value pairs
languages = {'python', 'ruby', 'python', 'c'}
print(languages)




