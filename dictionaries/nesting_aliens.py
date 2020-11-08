"""Nesting
Sometimes you'll want to store a set of dictionaries in a list or a list of items
as a value in a dictionary. This is called nesting. You can nest a set of dictionaries
inside a list, a list of items inside a dictionary, or even a dictionary inside
another dictionary."""

# How can you manage a fleet of aliens? One way is to make a list of aliens in which
# each alien is a dictionary of information about that alien.

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens:
print("\nThe first 5 aliens:")
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been crated.
print("Total number of aliens: " + str(len(aliens)))

# When it's time to change colors, we can use a for loop and an if statement to
# change the color of aliens.
for alien in aliens[:3]:
    # If the alien is green, we change the color to 'yellow', the speed to 'medium', and
    # the point value to 10.
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    # You could expand this loop by adding an elif block that turns yellow aliens into red,
    # fast-moving ones worth 15 points each.
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

print("\nThe first 5 aliens:")
for alien in aliens[:5]:
    print(alien)
print("...")
# It's common to store a number of dictionaries in a list when each dictionary contains many
# kinds of information about one object.
