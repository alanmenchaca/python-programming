"""Appending to a File
If you want to add content to a file instead of writing over existing content, you can open
the file in append mode. When you ope a file in append mode, Python doesn't erase the file
before returning the file object. Any lines you write to the file will be added at the end
of the file. If the file doesn't exist yet, Python will create an empty file for you."""
filename = 'programming.txt'

with open(filename, 'at') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
# We end up with the original contents of the file, followed by the new content we just added.
