"""Making an Instance from a Class
Think of a class as a set of instructions for how to make an instance. The class Dog
is a set of instructions that tells Python how to make individual instances representing
specific dogs."""
from dog import Dog

# Making an Instance from a Class
# We tell Python to create a dog whose name is 'willie' and whose age is 6. When Python
# reads this line, it calls the __init__() method in Dog with the arguments 'willie' and 6.
# The __init__() method creates an instance representing this particular dog and sets the
# name and age attributes using the values we provided.
my_dog = Dog('willie', 6)
# The __init__() method has no explicit return statement, but Python automatically returns
# an instance representing this dog. We store that instance in the variable my_dog. The
# naming convention is helpful here; we can usually assume that a capitalized name like
# Dog refers to a class, and a lowercase name like my_dog refers to a single instance
# created from a class.

# Accessing Attributes
# To access the attributes of an instance, you use dot notation. Dot notation finds
# the attribute name associated with my_dog. This is the same attribute referred to
# as self.name in the class.
print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")
