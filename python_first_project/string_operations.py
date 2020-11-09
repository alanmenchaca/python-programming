message = "Hello Python Crash Course world!"
print(message)
# We've added a variable named message. Every variable holds a value, which
# is the information associated with that variable. In this case the value is
# the text "Hello Python Crash Course world!"

message = 'This is a string.'
# We can change the value of a variable in our program at any time,
# and Python will always keep track of its current value.

# Naming and Using Variables
# - Variables names can contain only letter, numbers, and underscores.
#    They can start with a letter or an underscore, but not with a number.
# - Spaces are not allowed in variables names, but underscores can be used
#    to separate words in variable names.
# - Avoid using Python keywords and function names as variable names; that is,
#    do not use words that Python has reserved for a particular programmatic
#    purpose, such as the word print.
# - Variable names should be short but descriptive.

# Changing Case in String with Methods
name = "ada lovelace"
print(name.title())
# title() displays each word in title case, where each word begins with a capital letter
print("Name in uppercase: " + name.upper())
print("Name in lowercase: " + name.lower())
# We can change a string to all uppercase or all lowercase letters

# Combining or Concatenating String
first_name = "ada"
last_name = "lovelace"
full_name = (first_name + " " + last_name).title()

# Adding Whitespace to Strings with Tabs or Newlines
print("Hello, " + full_name + "!")
# Python uses the plus symbol (+) to combine strings. This method of combining strings
# is called concatenation.
print(f"Hello, {full_name}!")
print("Hello, {}!".format(full_name))
print("Hello, %s!" % (full_name))

# To add a newline in a string, we use the character combination \n
print("\n* Languages:\n\t- Python\n\t- C++\n\t- JavaScript")
# We can also combine tabs and newlines in a single string.
# The string "\n\t@ tells Python to move a new line, and start the next line with a tab.

# Stripping Whitespace
favorite_lenguage = 'python '.rstrip()
favorite_lenguage = ' python'.lstrip()
# We can strip whitespace from both sides at once using strip()
favorite_lenguage = ' python '.strip()
print(favorite_lenguage)

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
