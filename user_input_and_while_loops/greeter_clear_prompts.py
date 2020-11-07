"""Writing Clear Prompts
Each time you use the input() function, you should include a clear, easy-to-follow
prompt that tells the user exactly what kind of information you're looking for."""

# name = input("Please enter your name: ")
# print("Hello, %s!" % name)

# Sometimes you'll want to write a prompt that's longer than one line. You can store
# your prompt in a variable and pass that variable to the input() function. This allows
# you to build your prompt over several lines, then write a clean input() statement.
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
# In the second line, the operator += takes the string that was stored in prompt and
# adds the new string onto the end.

name = input(prompt)
print("Hello, %s!" % name)

# Using int() to Accept Numerical Input
# Whe we use the input() function, Python interprets everything the user enters as
# a string.
age = input("\nHow old are you? ")
# The int() function converts a string representation of a number to a numerical
# representation.
age = int(age)

# Python can run the conditional test: it compares age and 18 to see if age is
# greater than or equal to 18. This test evaluates to True.
print("Age > 18? %s" % (age > 18))
