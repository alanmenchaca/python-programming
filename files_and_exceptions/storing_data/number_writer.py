# Using json.dump() and json.load()
import json

# We first import the json module and then create a list of number to work with.
numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
# It's customary to use the file extension .json to indicate that the data in the file is stored
# in the JSON format. We open the file in write mode, which allows json to write the data to the
# file.
with open(filename, 'wt') as f_obj:
    # We use the json.dump() function to store the list numbers in the file numbers.json
    json.dump(numbers, f_obj)
