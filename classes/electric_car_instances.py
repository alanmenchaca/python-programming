from my_car import Car 


# Instances as Attributes
# When modeling something from the real world in code, you may find that you're adding
# more and more detail to a class. In this situation, you might recognize that part of
# one class can be written as a separate class. You can break your large class into
# smaller classes that work together.

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        # This line tells Python to create a new instance of Battery (with a default
        # size of 70, because we're not specify a value) and store that instance in
        # the attribute self.battery. This will happen This will happen every time the
        # __init__() method is called; any ElectricCar instance will now have a Battery
        # instance created automatically.
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            self.range = 240
        elif self.battery_size == 85:
            self.range = 270

        message = f"This car can go approximately {self.range}"
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

