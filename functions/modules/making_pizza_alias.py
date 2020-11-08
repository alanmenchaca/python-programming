"""Using as to Give a Function an Alias
If the name of a function you're importing might conflict with an existing name in
your program or if the function name is long, you can use a short, unique alias-an
alternate name similar to a nickname for the function. You'll give the function this
special nickname when you import the function."""

# The import statement shown here renames the function make_pizza() to mp() int this
# program. Any time we want to call make_pizza() we can simply write mp() instead, and
# Python will run the code in make_pizza() while avoiding any confusion with another
# make_pizza() function you might have writen this program file
from pizza_args import make_pizza as mp

mp(16, 'pepperoni')
mp(16, 'mushrooms', 'green peppers', 'extra cheese')

# The general syntax for providing an alias is:
# from module_name import function_name as fn
