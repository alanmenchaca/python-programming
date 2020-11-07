"""Slicing a List
To make a slice, you specify the index of the first and last elements you want
to work with. As with the range() function, Python stops one item before the
second index you specify. To output the first three elements in a list, you would
 request indices 0 through 3, which would return elements 0, 1, and 2."""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Players from 0 to 2: " + str(players[0:3]))

# We can generate any subset of a list.
print("Players from 1 to 3: " + str(players[1:4]))

# If you omit the first index in a slice, Python automatically starts your slice
# at the beginning of the list.
print("Players from the beginning to 3: " + str(players[0:4]))

# If you want all items from the third item through the last item, you can start
# with index 2 and omit the second item.
print("Player from 2 to the end: " + str(players[2:]))

# If we want to output the last three players on the roaster, we can use the slice:
print("Last three players: " + str(players[-3:]))
# This prints the names of the last three players and would continue to work as the
# list of players changes in size.

# Looping Through a Slice
# You can use a slice in a for loop if you want to loop through a subset of the
# elements in a list.
print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())
