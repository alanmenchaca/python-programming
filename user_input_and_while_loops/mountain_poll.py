"""Filling a Dictionary with User Input
We can prompt for as much input as you need in each pass through a while loop.
Let's make a program in which each pass through the loop prompts for the participant's
name and response. We'll store the data we gather in a dictionary, because we want
to connect each response with a particular user."""

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary:
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

    # Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print("%s would like to climb %s" % (name, response))

# The program first defines an empty dictionary (responses) and sets a flag (polling
# _active) to indicate that polling is active. As long as polling_active is True,
# Python will run the code in the while loop.
