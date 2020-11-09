"""Handling the ZeroDivisionError Exception
print(5 / 0)
The error reported in the traceback, ZeroDivisionError, is an exception object. Python
creates this kind of object in response to a situation where it can't do what we ask it to.
When this happens, Python stops the program and tells us the kind of exception that was
raised."""

# Using try-except Blocks
# When tou think an error may occur, you can write a try-except block to handle the exception
# that might be raised. You tell Python to try running some code, and tou tell it what to do
# if the code results in a particular kind of exception.
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
# We put print(5 / 0), the line that caused the error, inside a try block. If the code in a
# try block works, Python skips over the except block. If the code error in the try block
# causes an error, Python looks for an except block whose error matches the one that was
# raised and runs the code in that block.
