"""Many reasons exist to store a set of numbers. Lists are ideal for storing sets
of numbers, and Python provides a number of tools to help you work efficiently with
introducing_lists of numbers. As a result, you'll be able to work with introducing_lists of any length,
including those with thousands or even millions of items."""

# Using the range() Function
# Python's range() function makes it easy to generate a series of numbers.
for value in range(1, 5):
    print(value)
# The range() function causes Python to start counting at the first value you give it,
# and it stops reaches the second value you provide. Because it stops at that second
# value, the output never contains the end value.

# Using range() to Make a List of Numbers
# If you want to make a list of numbers, you can convert the results of range() directly
# into a list using the list() function. When you wrap list() around a call to the range()
# function, the output will be a list of numbers
numbers = list(range(1, 6))
print(numbers)

# We can also use the range() function to tell Python to skip numbers in a given range.
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# You can create almost any set of numbers you want to using the range() function
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# Simple statistic with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("The smallest item: " + str(min(digits)))
print("The biggest item: " + str(max(digits)))
print("The sum of a 'start' values: " + str(sum(digits)))
