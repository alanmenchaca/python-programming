# Saving and Reading User-Generated Data
# Saving data with json is useful when you;re working with user-generated data, because if you
# don't store your user's information somehow, you'll lose it when the program stops running.

import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'wt') as f_obj:
    # We prompt for a username to store. Next, we use json.dump() passing it a username and a file
    # object, to store the username in a file.
    json.dump(username, f_obj)
    # We print a message informing the user that we've stored their information.
    print(f"We'll remember you when you come back {username}!")
