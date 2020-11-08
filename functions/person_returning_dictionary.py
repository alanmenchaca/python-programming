"""Returning a Dictionary
A function can return any kind of value you need it to, including more complicated
data structures like lists and dictionaries."""


def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person


# This function takes in simple textual information and puts it into a more meaningful
# data structure that lets you work with the information beyond just printing it.
musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


# We add a new optional parameter age to the function definition and assign the parameter
# an empty default value. If the function call includes a value for this parameter, the
# value is stored in the dictionary.
musician = build_person('jimi', 'hendrix', age='27')
