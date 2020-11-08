"""Storing Your Functions in Modules
One advantage of functions is the way they separate blocks of code from your main program.
By using descriptive names for your functions, your main program will be much easier to follow.
You can go a step further by storing your functions in a separate file called a module and then
importing that module into your program. An import statement tells Python to make the code in a
module available in the currently running program file."""

# Importing an Entire Module
# To start importing functions, we first need to create a module. A module is a file ending in
# .py that contains the code you want to import into your program.
import pizza_args

# We'll make a separate file called making_pizza_module.py this file imports the module we just
# created and then makes two calls to make_second_pizza()
pizza_args.make_second_pizza(16, 'pepperoni')
pizza_args.make_second_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# When python reads this file, the line import pizza_args tells Python to open the file pizza_args.py
# and copy all the functions from it into this program.
# This first approach to importing, in which you simply write import followed by the name of the module,
# makes every function from the module available in your program.

# Storing your functions in a separate file allows you to hide the details of your program's code
# and focus on its higher-level logic. It also allows you to reuse functions in many different
# programs. When you store your functions in separate files, you can share those files with other
# programmers without having to share your entire program.
