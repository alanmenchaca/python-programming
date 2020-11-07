"""Introducing while loops
The for loop takes a collection of items and executes a block of code once for
each item in the collection. In contrast, the while loop runs as a long as, or
while, a certain condition is true."""

# You can use a while loop to count up through a series of numbers
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1
# We start counting from 1 by setting the value of current_number to 1. The while
# loop is then set to keep running as long as the value of current_number is less
# than or equal to 5.
# The code inside the loop prints the value of current_number and then adds 1 to
# that value with current_number += 1. (The += operator is shorthand for
# current_number = current_number + 1
