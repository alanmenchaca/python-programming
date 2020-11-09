"""Is Your Birthday Contained in Pi?
I've always been curious to know if my birthday appears anywhere in the digits of pi.
We can use the program we just wrote to find out if someone's birthday appears anywhere
in the first million digits of pi."""
filename = 'pi_million_digits.txt'

with open(filename, 'rt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line

# We prompt for the user's birthday, and then we check if that string is in pi_string.
birthday = input("Enter you birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
