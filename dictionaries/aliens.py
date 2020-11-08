"""Working with dictionaries
A dictionary in Python is a collection of key-value pairs. Each key is connected
to a value, and you can use a key to access the value associated with that key.
A key's value can be a number, a string, a list, or even another dictionary.
In fact, you can use any object that you can create in Python as a value in a
dictionary.
In Python, a dictionary is wrapped in braces, {}, with a series of key-values
pairs inside the braces."""

alien_0 = {'color': 'green', 'points': 5}
# A key-value pair is a set of values associated with each other. When you provide
# a key, Python returns the value associated with that key
# The string 'colon' is a key in this dictionary, and its associated value is 'green'.

# Accessing Values in a Dictionary
# To get the value associated with a key, give the name of the dictionary and then place
# the key inside a set of square brackets.
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Adding New Key-Value Pairs
# Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary
# at any time. To add a new key-value pair, you would give the name of the dictionary followed
# by the new key in square brackets along with the new value.
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
# The final version of the dictionary contains four key-value pairs.
# Notice that the order of the key-value pairs doesn't match the order in which we added them.
print(alien_0)

# Starting with an Empty Dictionary
# It's sometimes convenient, or even necessary, to start with an empty dictionary and then add
# each new item to it.
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying Values in a Dictionary
# To modify a value in a dictionary, give the name of the dictionary with the key in square
# brackets and then the new value you want associated with that key.
print("\nThe alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# -------------------------------------------------------------------------------------------------------
# For a more interesting example, let's track the position of an alien that can move at different
# speeds. We'll store a value representing the alien's current speed and then use it to determine
# how far to the right the alien should move.
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("\nOriginal x-position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
# This technique is pretty cool: by changing one value in the alien's dictionary,
# you can change the overall behavior of the alien.

# Removing Key-Value Pairs
# When you no longer need a piece of information that's stored in a dictionary, you can use the del
# statement to completely remove a key-value pair. All del needs is the name of the dictionary and
# the key that you want to remove.
alien_0 = {'color': 'green', 'points': 5}
print("\n" + str(alien_0))

del alien_0['points']
print(alien_0)
# Be aware that the deleted key-value pairs is removed permanently.
