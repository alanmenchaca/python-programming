"""Rather than breaking out of a loop entirely without executing the rest of
its code, you can use the continue statement to return to the beginning of the
loop based on the result of a conditional test."""

current_number = 0
# The if statement checks the modulo of current_number and 2. If the modulo is
# 0 (which means current_number is divisible by 2), the continue statement tells
# Python to ignore the rest of the loop and return to the beginning.
while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        continue

    # If the current_number is not divisible by 2, the rest of the loop is executed
    # and Python prints the current number.
    print(current_number)

# To avoid writing infinite loops, test every while loop and make sure the loop stops
# when you expect it to. If you want your program to end when the user enters a certain
# input value, run the program and enter that value.
