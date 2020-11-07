"""How do you use the int() function in an actual program?
The program can compare height to 36 because height = int(height) converts
the input value to a numerical representation before the comparison is made.
If the number entered is greater than or equal to 36, we tell the user that
they're tall enough."""

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
# When you use numerical input to do calculations and comparisons, be sure to
# convert the input value to a numerical representation first.
