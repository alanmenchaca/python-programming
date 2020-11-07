"""Using a flag
For a program that should run only as many conditions are true, you can define
one variable that determines whether or not the entire program is active. The
variable, called a flag, acts as a signal to the program. We can write our
programs so they run while the flag is set to True and stop running when any
of several events sets the value of the flag to False."""

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
# This is useful in complicated programs like games in which there may be many
# events that should each make the program stop running.
