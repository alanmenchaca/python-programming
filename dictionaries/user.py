"""Looping Through a Dictionary
A single Python dictionary can contain just a few key-value pairs or millions of pairs.
Because a dictionary can contain large amounts of data, Python lets you loop through a
dictionary. You can loop through all of a dictionary's key-value pairs, through its keys,
or through its values."""

# Looping Through All Key-Value Pairs
user_0 = {
    'username': 'efermi',
    'first': 'ernico',
    'last': 'fermi'
}

# The items() method returns a list of key-value pairs.
# The for loop then stores each of these pairs in the two variables provided.
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
