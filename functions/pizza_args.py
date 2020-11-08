"""Passing an Arbitrary Number of Arguments
Sometimes you won't know ahead of time how many arguments a function needs to accept.
Python allows you a function to collect an arbitrary number of arguments from the
calling statement"""


# The asterisk in the parameter name *toppings tells Python to make an empty tuple
# called toppings and pack whatever values it receives into this tuple.
def make_pizza(*toppings):
    """Summarize tbe pizza we are about to make."""
    print("\nMaking the pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


# Python packs the arguments into a tuple, even if the function receives only one value.
make_pizza('pepperoni')
# This syntax works no matter how many arguments the function receives.
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Mixing Positional and Arbitrary Arguments
# If you want a function to accept several different kinds of arguments, the parameter
# that accepts an arbitrary number of arguments must be placed last in the function
# definition. Python matches positional and keyword arguments first and then collects
# any remaining arguments in the final parameter.
def make_second_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {str(size)}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


# In the function definition, Python stores the first value it receives in the parameter
# size. All other values that come after are stored in the tuple toppings. The function
# calls include an argument for the size first, followed by as many toppings as needed.
make_second_pizza(16, 'pepperoni')
make_second_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
