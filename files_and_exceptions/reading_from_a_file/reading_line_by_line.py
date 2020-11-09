"""Reading line by line
When you're reading a file, you'll often want to examine each line of the file. You might
be looking for certain information in the file, or you might want to modify the text in the
file in some way."""

filename = 'pi_digits.txt'

# We store the name of the file we're reading from in the variable filename. This is a common
# convention when working with files. Because the variable filename doesn't represent the actual
# file- it's just a string telling Python where to find the file- you can easily swap out
# 'pi_digits.txt' fot the name of another file you want to work with.
with open(filename, 'rt') as file_object:
    # We use the with syntax to let Python open and close the file properly. To examine file's
    # contents, we work through each line in the file in the file by looping over the file object.
    for line in file_object:
        # The print statement adds its own newline each time we call it, so we end up with two
        # newline characters at the end of each line: one from the file and one from the print
        # statement. Using rstrip() on each line in the print statement eliminates these extra
        # blank lines:
        print(line.rstrip())
