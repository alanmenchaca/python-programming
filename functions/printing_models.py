"""Modifying a List in a Function
When you pass a list to a function, the function can modify the list. Any changes made to
the list inside the function's body are permanent, allowing you to work efficiently even
when you're dealing with a large amounts of data."""


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    # Display all completed models.
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
# This example demonstrates the idea that every function should have one specific job. The first
# function prints each design, and the second displays the completed models. This is more
# beneficial than using one function to do both jobs. If you're writing a function and notice
# the function is doing too many different tasks, try to split the code into two functions

# Preventing a Function from Modifying a List
# Sometimes you'll want to prevent a function from modifying a list.
# Example: function_name(list_name[:])
# This splice notation [:] makes a copy of the list to send to the function.

# print_models(completed_designs[:], completed_models)
# You can preserve the contents of a list by passing a copy of it to your functions, you should
# pass the original list to functions unless you have a specific reason to pass a copy. It's more
# efficient for a function to work with an existing list to avoid using the time and memory
# needed to make a separate copy, especially when you're working with large lists.
