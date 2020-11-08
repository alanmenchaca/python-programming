"""A list in a dictionary
Rather than putting a dictionary inside a list, it's sometimes useful to
put a list inside a dictionary."""

# The list of toppings is a value associated with the key 'toppings'. To use
# the items in the list, we give the name of the dictionary and the key
# 'toppings', as we would any value in the dictionary.

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
# We can nest a list inside a dictionary any time we want more than one value to be
# associated with a single key in a dictionary.
