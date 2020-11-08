"""Classes (Object-oriented programming) 
Object-oriented programming is one of the most effective approaches to writing
software. In object-oriented programming you write classes that represents real-world
things and situations, and you create objects based on these classes. Making an object
from a class is called instantiation, and you work with instances of a class."""


class Dog:
    """A simple attempt to model a dog."""

    # Creating and Using a Class
    # You can model almost anything using classes. This class will tell Python how to
    # make an object representing a dog. After our class is written, we'll use it to
    # make individual instances, each of which represents one specific dog.

    # The __init__ method
    # The __init__ method is a special method Python runs automatically whenever we create
    # a new instance based on the Dog class. This method has two leading underscores and two
    # trailing underscores, a convention that helps prevent Python's default method names
    # from conflicting with your method names.
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        # The self parameter is required in the method definition, and it  must come first
        # before the other parameters. It must be included in the definition because when Python
        # calls this __init__ method later (to create an instance of Dog), the method call
        # will automatically pass the self argument.
        self.name = name
        # Any variable prefixed with self is a variable to every method in the class, and we'll
        # also be able to access these variables through any instance created from the class.
        # self.name = name takes the value stored in the parameter name and stores it in the
        # variable name, which is then attached to the instance being created.
        self.age = age

    # Every method call associated with a class automatically passes self, which is a reference
    # to the instance itself; it gives the individual instance access to the attributes and
    # methods in the class.
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name.title()} rolled over!")
