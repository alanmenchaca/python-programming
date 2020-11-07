"""How to input() Function Works
The input() function pauses your program and waits for the user to enter some
text. Once Python receives the user's input, it stores it in a variable to make
it convenient for you to work with."""

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."

message = ""
# We'll define a quit value and then keep the program running as long as the user
# has not entered the quit value
while message != 'quit':
    # As long as the user has no entered the word 'quit', the prompt is displayed
    # again and Python waits for more input.
    message = input(prompt)
    print(message)
# The first time through the loop, message is just an empty string, so Python
# enters the loop. At message = input(prompt), Python displays the prompt and waits
# for the user to enter their input. Whatever the enter is stored in message and
# printed: then, Python reevaluates the condition in the while statement.

# The input() function takes one argument: the prompt, or instructions, that we
# want to display to the user so they know what to do.
