"""Keyword Arguments
A keyword argument is a name-value pair that you pass to a function. You directly
associate the name and the value within the argument, so when you pass the argument
to the function, there's no confusion. Keyword arguments free you from having to
worry about correctly ordering your arguments in the function call, and they clarify
the role of each value in the function call."""


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")


# The function describe_pet() hasn't changed. But when we call the function, we
# explicitly tell Python which parameter each argument should be matched with.
describe_pet(animal_type='hamster', pet_name='harry')
# The order of keyword arguments doesn't matter because Python knows where each
# value should go.
describe_pet(pet_name='harry', animal_type='hamster')


# Default Values
# When writing a function, you can define a default values for each parameter. If
# an argument for a parameter is provided in the function call. Python uses the
# argument value. If not, it uses the parameter's default value. So when you
# define a default value for a parameter, you can exclude the corresponding argument
# you'd usually write in the function call.
def descibe_pet_default(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")


# The order of the parameters had to be changed. Because the default value makes it
# unnecessary to specify a type of animal as an argument, the only argument left in
# the function call is the pet's name.
# Python still interprets this as a positional argument, so if the function is
# called with just a pet's name, that argument will match up with the first
# parameter listed in the function definition.
descibe_pet_default(pet_name='Willie')
# Because an explicit argument for animal_type is provided, Python will ignore the
# parameter's default value.

# When you use default values, any parameter with a default value needs to be listed
# after all the parameters that don't have default values. This allows Python to
# continue interpreting positional arguments correctly.
