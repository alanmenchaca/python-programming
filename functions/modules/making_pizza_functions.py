"""Importing Specific Functions
You can also import a specific function from a module."""
# The general syntax for import a specific function is:
# from module_name import function_name
from pizza_args import make_pizza, make_second_pizza

# You can import as many functions as you want from a module by separating each function's
# name with a comma
# from module_name import function_0, function_1, function_2

make_pizza(16, 'pepperoni')
make_second_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# With this syntax, you don't need to use the dot notation when you call a function. Because
# we've explicitly imported the function make_pizza() in the import statement, we can call it
# by name when we use the function.
