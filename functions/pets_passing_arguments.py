"""Passing Arguments
Because a function definition can have multiple parameters, a function call may need
multiple arguments. You can pass arguments to your functions in a number of ways. You
can use positional arguments, which need to be in the same order the parameters were
written; keyword arguments, where each argument consists of a variable name and a value;
and lists and dictionaries of values."""


# Positional arguments
# Whe you call a function, Python must match each argument in the function call with a
# parameter in the function definition. The simplest way to do this based on the order
# of the arguments provided. Values matched up this way are called positional arguments.
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# The definition shows that this function needs a type of animal and the animal's name.
# When we call describe_pet(), we need to provide an animal type and a name, in that order.
describe_pet('hamster', 'harry')

# Multiple Function Calls
# You can call a function as many times as needed.
# In this second function call, we pass describe_pet() the arguments 'dog' and 'willie'.
describe_pet('dog', 'willie')
# The code describing a pet is written once in the function. Then, anytime you want to
# describe a new pet, you call the function with the new pet's information. Python works
# through the arguments you provide when calling the function and matches each one with
# the corresponding parameter in the function's definition.

# Check to make sure the order of the arguments in your function call matches the order
# of the parameters in the function's definition.
