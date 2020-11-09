"""Refactoring
Often, you'll come to a point where you code will work, but you'll recognize that you could
improve the code by breaking it up into a series of functions that have specific jobs. This
process is called refactoring. Refactoring makes your code cleaner, easier to understand,
and easier to extend."""
import json


def get_stored_username():
    """Get stored username if available."""
    # This function retrieves a stored username and returns the username if it finds one.
    # If the file username.json doesn't exist, the function returns None. This is a good
    # practice: a function should either return the value you're expecting, or it should
    # return None. This allows us to perform a simple test with the return value of the
    # function.
    filename = 'username.json'

    try:
        with open(filename, 'rt') as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is you name? ")
    filename = 'username.json'

    with open(filename, 'wt') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()

    # We print a welcome back message to the user if the attempt to retrieve a username was
    # successful, and if it doesn't, we prompt for a new username.
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when come back, {username}!")


greet_user()

# Each function in this final version of remember_me_user.py has a single, clear purpose.
# We call greet_user(), and that function prints an appropriate message: it either welcomes
# back and existing user or greets a new user. It does this by calling get_stored_username(),
# which is responsible only for retrieving a stored username if one exists. Finally,
# greet_user() calls get_new_username() amd storing it. This compartmentalization of work is
# an essential part of writing clear code that will be easy to maintain and extend.
