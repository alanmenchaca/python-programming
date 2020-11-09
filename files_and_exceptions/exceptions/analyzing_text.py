"""Analyzing Text
You can analyze text files containing entire books."""
filename = 'alice.txt'

try:
    with open(filename, 'rt') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = f"Sorry, the file {filename} does not exist."
    print(msg)
else:
    # Count the approximate number of words in the file.
    # The split() method separates a string into parts into wherever it finds a space and stores
    # all the parts of the string in a list. The result is a list of words from the string, although
    # some punctuation may also appear with some of the words. To count the number of words in
    # Alice in Wonderland, we'll use split on the entire text.
    words = contents.split()
    # When we use len() on this list to examine its length, we get a good approximation of the
    # number of words in the original string.
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
    # The count is little high because extra information is provided by the publisher in the text
    # file used here.
