"""Using exceptions to Prevent Crashes
Handling errors correctly is specially important when the program has more work to do after
the error occurs. This happens often in programs that prompts users for input. If the program
responds to invalid input appropriately, it can prompt for more invalid input instead of
crashing."""

# This program prompts the user to input a first_number and, if the user does not enter
# the q to quit, a second_number. We then divide these two numbers to get an answer.
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break

    # The else Block
    # Whe can make this program more error resistant by wrapping the line that might produce
    # errors in a try-except block. The error occurs on the line that performs the division,
    # so that's where we'll put the try-except block.
    try:
        # We ask Python to try to complete the division operation in the try block, which
        # includes only the code that might cause an error. Any code that depends on the try
        # block succeeding is added to the else block.
        answer = int(first_number) / int(second_number)
        # The except block tells Python how to respond when a ZeroDivisionError arises.
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

    # The try-except-else block works like this: Python attempts to run the code in the try
    # statement. The only code that should go in a try statement, is a code that might cause
    # an exception to be raised. Sometimes you'll have additional code that should run only
    # if the try block was successful; this code goes in the else block. The except block tells
    # Python what to do in case a certain exception arises when it tries to run the code in the
    # try statement.
