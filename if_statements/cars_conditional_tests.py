"""A Simple Example: The following short example shows how if test let you respond
to special situations correctly."""

# The following code loops through a list of car names and looks for the value "bmw".
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# The loop in this example first checks if the current value of car is 'bmw'. If it iz,
# the value is printed in uppercase. If the value of car is anything other than 'bmw', it's
# printed in title case

# Conditional Tests
# At the heart of evert if statement is an expression that can be evaluated as True or False
# and is called a conditional test. Python uses the values True and False to decide whether
# the code in an if statement should be executed.

# Checking for Equality
# The simplest conditional test checks whether the value of a variable is equal to the value
# of interest
equality = str((car[0] == 'bmw'))
print("\nChecking for Equality (car[0] == 'bmw'): " + equality)

# Ignoring Case When Checking for Equality
# Testing for equality is case sensitive in Python. For example, two values with different
# capitalization are not considered equal.
car = 'Audi'
equality = str(car == 'audi')
print("car = 'Audi'")
print("Checking for Equality (car == 'audi'): " + equality)

equality = str(car.lower() == 'audi')
# The lower() function doesn't change the value that was originally stored in car, so you can
# do this kind of comparison without affecting the original variable.
print("\ncar.lower() = 'audi'")
print("Checking for Equality (car.lower() == 'audi'): " + equality)

# Websites enforce certain rules for the data that users enter in a manner similar to this.
# When someone submits a new username, that new username is converted to lowercase and compared
# to the lowercase versions of all existing usernames. During this check, a username like 'Jhon'
# will be rejected if any variation of 'jhon' is already in use.
