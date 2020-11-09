import json

# We'll write a program that uses json.load() to read the list back into memory.
filename = 'numbers.json'

with open(filename, 'rt') as f_obj:
    # We use the json.load() function to load the information stored in numbers.json,
    # and we store it in the variable numbers.
    numbers = json.load(f_obj)

print(numbers)
# This is a simple way to share data between two programs.
