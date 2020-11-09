import json

filename = 'username.json'
with open(filename, 'rt') as f_obj:
    # we use json.load() to read the information stored in username.json into the variable
    # username. Now we've recovered the username, we can welcome them back.
    username = json.load(f_obj)
    print(f"Welcome back, {username}!")