"""Passing a List
You'll often find it useful to pass a list to a function, whether it's a list of
names, numbers, or more complex objects, such as dictionaries. When you pass a list
to a function, the function gets direct access to the contents of the list."""


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
# We define greet_users() so it expects a list of names, which it stores in the
# parameter names. The function loops through the list it receives and prints
# a greeting to each user.
greet_users(usernames)
