# Reading an Entire File
with open('pi_digits.txt', mode='rt') as file_object:
    # To do any work with a file, even just printings its contents, you first need to open the
    # file to access it. The open() function needs one argument: the name of the file you want to
    # open. Python looks for this file in the directory where the program that's currently being
    # executed is stored.
    contents = file_object.read()
    # The open() function returns an object representing the file. Here, open('pi_digits.txt')
    # returns an object representing pi_digits.txt. Python stores this object in file_object,
    # which we'll work with later in the program.
    print(contents)
    # You could open and close the file by calling open() and close(), but if a bug in your
    # program prevents the close() statement from being executed, the file may never close.
    # And if you close() too early in you program, you'll find yourself trying to work with
    # a closed file (a file you can't access), which leads to more errors.
    # The keyword with closes the file once access to it is no longer needed.
