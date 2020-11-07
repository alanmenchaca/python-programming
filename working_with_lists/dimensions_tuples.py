"""Tuples: Defining a Tuple
Sometimes you'll want to create a list of items that cannot change. Tuples allow you
to do just that. Python refers to values that cannot change as immutable, and an
immutable list is called a tuple."""

# A tuple looks just like a list except you use parentheses instead of square brackets.
dimensions = (200, 500)
print(dimensions[0])
print(dimensions[1])

# We cannot do this
# dimension[0] = 250
# The code tries to change the value of the first dimension, but Python returns a type error.
# Basically, because we're trying to alter a tuple, which can't be done to that type of object,
# Python tells us we can't assign a new value to an item in a tuple.

# Looping through All Values in a Tuple
for dimension in dimensions:
    print(dimension)

# Writing over the a Tuple
# Although you can't modify a tuple, you can assign a new value to a variable that holds a tuple.
# So if we wanted to change our dimensions, we could redefine the entire tuple.
dimensions = (200, 500)
print("\nOriginal Dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)

# When compared with introducing_lists, tuples are simple data structures. Use them when you want to store a
# a set of values that should not be changed throughout the life of a program.
