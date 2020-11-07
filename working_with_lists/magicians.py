"""You'll often want to run through all entries in a list, performing the same task
with each item. When you want to do the same action with every item in a list, you
can use Python's for loop."""

magicians = ['alice', 'david', 'carolina']

# "For every magician in the list of magicians, print the magician's name and a message."
# The output shows a personalized message for each magician in the list.
for magician in magicians:
    # We printing a message to each magician, telling them that they performed a great trick.
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
# Every idented line following the line for magician in magicians is considered inside the
# loop, and each idented line is executed once for each value in the list.

# Doing something After a for loop.
# Usually, you'll want to summarize a block of output or move on to other work that your
# program must accomplish. Any lines of code after the for loop that are not idented are
# executed once without repetition.
print("Thank you, everyone. That was a great magic show!")

# Common Errors Identation:
#   - Forgetting to Ident
#   - Forgetting to Ident Additional Lines
#   - Identing Unnecessarily
#   - Forgetting the Colon
