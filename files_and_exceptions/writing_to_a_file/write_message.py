# Writing to an Empty File
# To write to a file, you need to call open() with a second argument telling Python that you
# want to write to the file.
filename = 'programming.txt'

with open(filename, 'wt') as file_object:
    # The first argument is the name of the file we want to open. The second argument, 'w', tell
    # Python that we want to open the file in write mode. You can open a file in read mode ('r'),
    # write mode ('w'), append mode ('a'), or a mode that allows you to read and write to the file
    # ('r+'). If you omit the mode argument, Python opens the file in read-only mode by default.
    file_object.write("I love programming.\n")
    # Writing Multiple Lines
    # The write() function doesn't add any newlines to the text you write. Including newlines in
    # your write() statements make each string appear on its own line.
    # You can also use spaces, tab character, and blank lines to format you output, just as you've
    # been doing with terminal-based output.
    file_object.write("I love creating new games.\n")
    # Be careful opening a file in write mode ('w') because if the file does exist, Python will
    # erase the file before returning the file object. Python can only write strings to a text
    # file. If you want to store numerical data in a text file, you'll have to convert the data
    # to string format first using the str() function.
