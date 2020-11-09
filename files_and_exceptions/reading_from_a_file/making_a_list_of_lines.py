"""Making a List of Lines from a File
When you use with, the file object returned by open() is only available inside the with block
that contains it. If you want to retain access to a file's contents outside the with block, you
can store the file's lines in a list inside the block and then work with that list. You can
process parts of the file immediately and postpone some processing for later in the program."""
filename = 'pi_digits.txt'

with open(filename, 'rt') as file_object:
    lines = file_object.readlines()

# The readlines() method takes each line from the file and stores it in a list. This list is then
# stored in lines. which we can continue to work with after the with block ends.
for line in lines:
    # Because each item in lines corresponds to each line in the file the output matches the
    # contents of the file exactly.
    print(line.rsplit())

# Working with a File's Contents
# After you've read a file into memory, yo can do whatever you with that data.
pi_string = ''
for line in lines:
    # We create a loop that adds each line of digits to pi_string and removes the newline character
    # from each line.
    pi_string += line.strip()

print('\n' + pi_string)
print(len(pi_string))
# When Python reads from a text file, it interprets all text in the file as a string. If you read in
# a number and want to work with that value in a numerical context, you'll have to convert it to an
# integer using the int() function or convert it to a float using the float() function.



