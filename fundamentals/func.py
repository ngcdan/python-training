def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name="Harry")
describe_pet(pet_name="Harry", animal_type='cat')

# Passing arbitrary number of arguments
def make_pizza(*toppings):
    for topping in toppings:
        print(topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

print("# Using arbitrary keyword arguments")
def build_profile(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

