"""Calling Methods
After we create an instance from the class Dog. we can use dot notation to call any
 method defined in Dog."""
from dog import Dog

my_dog = Dog('willie', 6)

# To call a method, give the name of the instance (in this case, my_dog) and the method
# you want to call, separated by dot. When Python reads my_dog.sit(), it looks for the
# method sit() in the class Dog and runs that code. Python interprets the line
# my_dog.roll_over() in the same way.
my_dog.sit()
my_dog.roll_over()

# This syntax is quite useful. When attributes and methods have been given appropriately
# descriptive names like name, age, sit(), and roll_over(), we can easily infer what a
# block of code, even one we've never seen before, is supposed to do.
