"""Importing All Functions in a Module
You can tell Python to import every function in a module by using the asterisk
(*) operator."""

# The asterisk in the import statement tells Python to copy every function from the module
# pizza into this program file. Because every function is imported, you can call each function
# by name without using the dot notation.
# However, it's best not to use this approach when you're working with larger modules that you
# didn't write: if the module has a function name that matches an existing name in your project,
# you can get some unexpected results. Python may see several functions or variables with the same
# name, and instead of importing all the functions separately, it will overwrite the functions.
from pizza_args import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# The best approach is to import the function or functions you want, or import the entire module
# and use the dot notation. This leads to clear code that's easy to read and understand.

# Functions should have descriptive names, and these names should use lowercase, letters and
# underscores. Descriptive names help you and others understand what your code is trying to do.
# Module names should use these conventions as well.
# Every function should have a comment that explains concisely what the function does. This comment
# should appear immediately after the function definition and use the docstring format. In a well-
# documented function, other programmers can use the function by reading only the description in
# the docstring.

# If your program or module has more than one function, you can separate each by two blank lines
# to make easier to see where one function ends and next one begins.
# All import statements should be written at the beginning of a file. The only exception is if you
# use comments at the beginning of your file to describe the overall program.
