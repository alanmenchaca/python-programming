"""Testing Multiple Conditions
Sometimes it's important to check all of the conditions of interest. In this case, you
should use a series of simple if statements with no elif or else blocks. This technique
makes sense when more than one condition could be True, and you want to act on every
condition that is True."""

requested_toppings = ['mushrooms', 'extra cheese']

# These three independent tests are valuated, both mushrooms and extra cheese are
# added to the pizza
print("Testing Multiple Conditions:")
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

# This code would not work properly if we used an if-elif-else block, because the code
# would stop running after only one test passes.
print("Finished making your pizza!\n")

# Checking for Special Items
# The pizzeria displays a message whenever a topping is added to your pizza, as it's
# begin made.
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

print("Checking for Special Items:")
for requested_topping in requested_toppings:
    # What if the pizzeria runs out of green peppers?
    # An if statement inside the for loop can handle this situation appropriately
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("- Adding " + requested_topping + ".")

print("Finished making your pizza!\n")

# Checking That a List Is Not Empty
# Soon we'll let users provide the information that's stored in a list, so we won't be able to
# assume that a list has any items in it each time a loop is run. In this situation, it's
# useful to check whether a list is empty before running a for loop.
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("- Adding " + requested_topping + ".")
else:
    # This list is empty in this case, so the output asks if the user really wants a plain pizza.
    print("Are you sure you want a plain pizza?\n")
# If the list is not empty, the output will show each requested topping being added to the pizza.


# Using Multiple Lists
# What if the costumer actually wants french fries on their pizza? You can use introducing_lists and if statements
# to make sure your input makes sense before you act on it.

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# The first is a list of available toppings at the pizzeria, and the second is the list of toppings that
# the user has requested. This time, each item in requested_toppings is checked against the list of
# available toppings before it's added to the pizza.

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("- Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("Finished making your pizza!")
