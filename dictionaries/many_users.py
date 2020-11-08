"""A Dictionary in a Dictionary
We can nest a dictionary inside another dictionary, but our code can get complicated
quickly when we do."""

# If we have several users for a website, each with a unique username, we can use the
# usernames as the keys in a dictionary. We can then store information about each user
# by using a dictionary as the value associated with their username.
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, userinfo in users.items():
    print("\nUsername: " + username)
    full_name = userinfo['first'] + " " + userinfo['last']
    location = userinfo['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

# Notice that the structure of each user's dictionary is identical. Although not required
# by Python, this structure makes nested dictionaries easier to work with. If each user's
# dictionary had different keys, the code inside the for loop would be more complicated.
