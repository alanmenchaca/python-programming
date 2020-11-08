"""Using a Function with a while loop"""


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# This is an infinite loop!
while True:
    # We want the user to able to quit as easily possible, so each prompt should offer a
    # way to quit. The break statement offers a straightforward way to exit the loop.
    print("\nPlease tell me your name:")
    # We add a message that informs the user how to quit, and then we break out of the
    # loop if the user enters the quit value at either prompt.
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
