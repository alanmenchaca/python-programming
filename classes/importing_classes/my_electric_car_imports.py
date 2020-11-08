# Storing Multiple Classes in a Module
from car import ElectricCar

# You can store as many classes as you need in a single module, although each class in a
# module should be related somehow.

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# When you instead move the class to a module and import the module, you still get all the
# the same functionality, but you keep your main program file clean and easy to read. You
# also store most of the logic in separate files; once your classes work as you want them
# to, you can leave those files alone and focus on the higher-level logic of your main program.
