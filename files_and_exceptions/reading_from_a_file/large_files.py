"""Large Files: One Million Digits
If we start with a text file that contains pi to 1,000,000 decimal places instead of just 30,
we can create a single string containing all these digits."""
filename = 'pi_million_digits.txt'

with open(filename, 'rt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line

# The output shows that we do indeed have a string containing a pi to 1,000,000 decimal places.
print(pi_string[:52] + "...")
print(len(pi_string))
# Python has no inherent limit of how much data you can work with; you can work with as much data
# as your system's memory can handle.
