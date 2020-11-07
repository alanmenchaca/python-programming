"""The if-elif-else Chain
Often, you'll need to test more than two possible situations, and to evaluate
these you can use Python's if-elif-else syntax. Python executes only one block
in an if-elif-else chain. It runs each conditional test in order until one passes.
When a test passes, the code following that test is executed and Python skips the
rest of the tests. Example:"""

# How can we use an if statement to determine a person's admission rate?
# * Admission for anyone under age 4 is free.
# * Admission for anyone between the ages of 4 and 18 is $5
# * Admission for anyone age 18 or older is $10
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")

# ------------------------------------------------------------------------------------------
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")
# The code produce the same output as the previous example, but the purpose of the
# if-elif-else chain is narrower. Instead of determining a price and displaying a message,
# it simply determines the admission price.

# Using Multiple elif Blocks
# You can use as many elif blocks in your code as you like. Let's say that anyone 65 or
# older pays half the regular admission, or $5.
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# Omitting the else Block
# Python does not require an else block at the end of an if-elif chain. Sometimes
# an else block is useful; sometimes it is clearer to use an additional elif
# statement that catches the specific condition of interest.
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")
# The else block is a catchall statement. It matches any condition that wasn't matched
# by a specific if or elif test, and that can sometimes include invalid or even malicious data.
# As a result, you'll gain extra confidence that your code will run only under the
# correct conditions.
