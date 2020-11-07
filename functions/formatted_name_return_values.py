"""Return Values
A function doesn't always have to display its output directly. Instead, it can process
some data and then return a value or set of values. The value the function returns
is called a return value. The return statement takes a value from inside a function
and sends it back to the line that called the function."""


# Returning a Simple Value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}."
    return full_name.title()


# When you call a function that returns a value, you need to provide a variable where
# the return value can be stored. In this case, the returned value is stored in the
# variable musician.
musician = get_formatted_name('jimi', 'hendrix')
print(f"Formatted name (without middle_name): {musician}")


# Making an argument optional
# Sometimes it makes sense to make an argument optional so that people using the
# function can choose to provide extra information only if they want to. You can se
# default values to make an argument optional.
def get_formatted_name_default(first_name, middle_name, last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name_default('john', 'lee', 'hooker')
print(f"Formatted name (with middle_name): {musician}")


# To make the middle name optional, we can give the middle_name argument an empty default
# value and ignore the argument unless the user provides a value.
# To make get_formatted_name() work without middle_name, we set the default value of
# middle_name to an empty string and move it to the end of the list of parameters.
def get_formatted_name_default(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


# The name is built from three possible parts. Because there's always a first and last name,
# these parameters are listed first in the function's definition. The middle name is optional,
# so it's listed last in the definition.
musician = get_formatted_name_default('jimi', 'hendrix')
musician = get_formatted_name_default('john', 'hooker', 'lee')
# Optional values allow functions to handle a wide range of use cases while letting function
# calls remain as simple as possible.
