"""Defining a function
This example shows the simplest structure of a function."""

# This is the function definition, which tells Python the name of the function and, if
# applicable, what kind of information the function need to do its job. The parentheses
# hold that information. In this case, the name of the function is greet_user(), and it
# needs no information to do its job, so its parentheses are empty.
def greet_user():
    # Any idented lines that follow def greet_user(): make up the body of the function.
    """Display a simple greeting"""
    # The text is a comment called a docstring, which describes what the function does.
    # Docstrings are enclosed in triple quotes, which Python looks for when it generates
    # documentation for the functions in your programs.
    print("Hello!")


# By adding username here you allow the function to accept any value of username you
# specify. The function now expects you to provide a value for username each time you
# to call it.
def greet_user_argument(username):
    """Display a simple greeting."""
    print("Hello, %s!" % username.title())


greet_user()
greet_user_argument('jesse')
# The variable username in the definition of greet_user() is an example of a parameter,
# a piece of information the function needs to do its job. The value 'jesse' in greet_
# user('jesse') is an example of an argument. An argument is a piece of information that
# is passed from a function call to a function.

# People sometimes speak of arguments and parameters interchangeably. Don't be sure
# surprised if you see the variables in a function definition referred to as argument
# or the variables in a function call referred to as parameters.
