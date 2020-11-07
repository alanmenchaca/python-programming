"""Equivalent Function Calls
Because positional argument, keywords arguments, and default values can all be
used together, often you'll have several equivalent ways to call a function."""


def descibe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")


# A dog name Willie
# With this definition, an argument always needs to be provided for pet_name, and this
# value can be provided using the positional or keyword format
descibe_pet('willie')
descibe_pet(pet_name='willie')

# A hamster named Harry.
# If the animal being described is not a dog, an argument for animal_type must be included
# in the call, and this argument can also be specified using the positional or keyword format.
descibe_pet('harry', 'hamster')
descibe_pet(pet_name='harry', animal_type='hamster')
descibe_pet(animal_type='hamster', pet_name='harry')

# It doesn't really matter which calling style you use. As long as your function calls
# produce the output you want, just use the style you find easiest to understand
