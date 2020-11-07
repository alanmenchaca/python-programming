"""If statements
Several different kinds of if statements exist, and your choice of which to use
depends on the number of conditions you need to test."""

# Simple if statements
# The simplest kind of if statement has one test and one action
age = 19

# All idented lines after an if statement will be executed if the test passes, and
# the entire block of idented lines will be ignored if the test does not pass.
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
# The conditional test passes, and both print statements are idented, so both lines
# are printed,

# if-else Statements
# Often, you'll want to take one action when a conditional test passes and different
# action in all other cases. Python's if-else syntax makes this possible.
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
# An if-else block is similar to a simple if statement, but the else statement allows
# you to define an action or set of actions that are executed when the conditional test fails.
