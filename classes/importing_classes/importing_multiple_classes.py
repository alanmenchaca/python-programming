"""Importing Multiple Classes from a Module
You can import as many classes as you need into a program file."""
from car import Car, ElectricCar

# You can import multiple classes from a module by separating each class with a comma.
# Once you've imported the necessary classes, you're free to make as many instances
# of class as you need.

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
