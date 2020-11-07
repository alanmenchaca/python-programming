"""Checking for Inequality
When you want to determine whether two values are not equal, you can combine an
exclamation point and an equal sign (!=)."""
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Checking Whether a Value is in a List
# To find out whether a particular value is already in a list, use the keyword in.
# Let's consider some code you might write for a pizzeria. We'll make a list of toppings
# a costumer has requested for a pizza and then check whether certain toppings are
# in a list.
requested_topping = ['mushrooms', 'onions', 'pineapple']
condition = str('mushrooms' in requested_topping)
print("Are there mushrooms in Requested toppings?: " + condition)

condition = str('pepperoni' in requested_topping)
print("Are there pepperoni in Requested toppings?: " + condition)
# The keyword in tells Python to check for the existence of 'mushrooms' and 'pepperoni'
# in the list requested_toppings.

# Numerical Comparisons
# Testing numerical values is pretty straightforward.
answer = 17

if answer != 42:
    print("That is not the correct answer, pleas try again!")

age = 19
print("\nage < 21?: " + str(age < 21))
print("age <= 21?: " + str(age <= 21))
print("age > 21?: " + str(age > 21))
print("age >= 21?: " + str(age >= 21))

# Checking Multiple Conditions
# You may want to check multiple conditions at the same time. Sometimes you might need
# two conditions to be True to take an action.

# Using and to Check Multiple Conditions
# To check whether two conditions are both True simultaneously, use the keyword and to
# combine the two conditional tests; if each test passes, the overall expressions evaluates
# to True. If either test fails or if both test fail, the expression evaluates to False.
age_0 = 22
age_1 = 18
print("\nMultiple Conditions (and)")
print("age_0 >= 21 and age_1 >= 21?: " + str((age_0 >= 21) and (age_1 >= 21)))

# Using or to Check Multiple Conditions
# The keyword or allows you to check multiple conditions as well, but it passes when either
# or both of the individual tests pass. An or expression fails only when both individual
# tests fail.
print("\nMultiple Conditions (or)")
print("age_0 >= 21 or age_1 >= 21?: " + str((age_0 >= 21) or (age_1 >= 21)))
print("age_0 < 21 or age_1 > 21?: " + str((age_0 < 21) or (age_1 > 21)))
