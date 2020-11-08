"""Working with Classes and Instances
You can use classes to represent many real-world situations. Once you write a class,
you'll spend most of your time working with instances created from that class. One of
the first tasks you'll want to do is modify the attributes of an instance directly or
write methods that update attributes in specific ways."""


class Car:
    """A simple attempt to represent a car."""

    # Our class will store information about the kind of car we're working with, and it
    # will have a method that summarizes this information.

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # Every attribute in a class needs an initial value, even if that value is 0 or an
        # empty string. In some cases, such as when setting a default value, it makes sense
        # to specify this initial value in the body of the __init__() method.
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    # It can be helpful to have methods that update certain attributes for you. Instead
    # of accessing the attribute directly, you pass the new value to a method that handles
    # the updating internally.
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        # If the new mileage, mileage, is greater than or equal to the existing mileage,
        # self.odometer_reading, you can update the odometer reading to the new mileage.
        # If the new mileage is less than the existing mileage, you'll get a warning that
        # you can't roll back an odometer.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    # Sometimes you'll want to increment an attribute's value by a certain amount rather
    # than set an entirely new value.
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        # The method increment_odometer() take in a number of miles, and adds this value
        # to self.odometer_reading.
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# You can change an attribute's value in the three ways; you can change the value directly
# through an instance, set the value through a method, or increment the value (add a certain
# amount to it) through a method. The simplest way to modify the value of an attribute is to
# access the attribute directly through an instance.
my_new_car.odometer_reading = 23

my_new_car.update_odometer(23)
my_new_car.read_odometer()

# ------------------------------------------------------------------------------------------
my_used_car = Car('subaru', 'outback', 2013)
print("\n" + my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# You can use methods like this to control how users of your program update values such as an
# odometer reading, but anyone with access to the program can set the odometer reading to any
# value by accessing the attribute directly.
