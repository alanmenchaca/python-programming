"""Removing All Instances of Specific Values from a List
Say you have a list of pets with the value 'cat' repeated several times. To remove
all instances of that value, you can run a while loop until 'cat' is no longer in
the list."""

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

# We start with a list containing multiple instances of 'cat'. After printing the
# list, Python enters the while loop because it finds the value 'cat'. in the list
# ate least once.
while 'cat' in pets:
    # Once inside the loop, Python removes the first instance of 'cat', returns to
    # the while line, and then reenters the loop when it finds that 'cat' is still
    # in the list.
    pets.remove('cat')

# It removes each instance of 'cat' until the value is no longer in the list, at which
# point Python exits the loop and prints the list again.
print(pets)
