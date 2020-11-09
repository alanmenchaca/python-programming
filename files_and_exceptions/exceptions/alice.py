"""Handling the FileNotFoundError Exception
One common issue when working with files is handling missing files. The file you're looking
for might be in a different location, the filename may be misspelled, or the file may no exist
at all. You can handle all of these situations in a straightforward wat with a try-except block."""

filename = 'alice.txt'

try:
    with open(filename, 'rt') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    # The code in the try block produces a FileNotFoundError, so Python looks for an except block
    # that matches that error. Python then runs the code in that block, and the result is a friendly
    # error message instead of a traceback.
    msg = f"Sorry, the file {filename} does not exist."
    print(msg)
    # The program has nothing more to do if the file doesn't exist, so the error-handling code doesn't
    # add much to this program.


