""" A List is a collection of items in a particular oder. You can make a list that
includes the letters of the alphabet, the digits from 0-9, or the names of all the
people in your family.
In Python, square brackets ([]) indicate a list, and individual elements in the list
are separated by comas."""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# If you ask Python to print a list, Python returns its representation of the list
print("Printing a list: " + str(bicycles))

# List are ordered collections, so you can access any element in a list by telling
# Python the position, or index, of the item desired.
# When we ask for a single item from a list. Python returns just that element.
print("\nFirst element of the list " + bicycles[0].title())

# Index Position Start at 0, Not 1
# Python considers the first item in a list to be at position 0, not position 1.
# This is true of most programming languages, and the reason has to do with how
# the list operations are implemented at a lower level
print("Second element of the list " + bicycles[1])
print("Fourth element of the list " + bicycles[3])
# This code returns the second and fourth bicycles in the list

# Python has a special syntax for accessing the last element in a list. By asking
# for the item at index -1. Python always returns the last item in the list.
print("Last item in the list " + bicycles[-1])
# The index -2 returns the second item from the end of the list, the index -3
# returns the third item from the end, and so forth.

# Using Individual Values from a List
message = "\nMy first bicycle was a {} ".format(bicycles[0].title())
print(message)
