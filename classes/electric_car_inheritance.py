"""If the class you're writing is a specialized version of another class you wrote,
you can use inheritance. When one class inherits from another, it automatically takes
on all the attributes and methods of the first class. The original class is called
parent class, and the new class is the child class. The child class inherits every
attribute and method from its parent class but it also free to define new attributes
and methods of its own."""

from my_car import Car


# When you create a child class, the parent class must be part of the current file and must
# appear before the child class in the file. We define the child class, ElectricCar. The
# name of the parent class must be included in parentheses in the definition of the child
# class.

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        # The super function is a special function that helps Python make connections between
        # the parent class and child class. This line tells Python to call the __init__() method
        # from ElectricCar's parent class, which gives an ElectricCar instance all the attributes
        # of its parent class. The name super comes from a convention calling the parent class
        # a superclass and the child class a subclass.
        super().__init__(make, model, year)
        # This attribute will be associated with all instances created from the ElectricCar class
        # but won't be associated with any instances of Car.
        self.battery_size = 70

    # Once you have a child class that inherits from a parent class, you can add any new attributes
    # and methods necessary to differentiate the child class from the parent class.

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


# The ElectricCar instance works just like an instance of Car, so now we can begin defining
# attributes and methods specific to electric cars.
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
# There's no limit to how much you can specialize the ElectricCar class. You can add as many
# attributes and methods as you need to model an electric car tho whatever degree of accuracy
# you need. An attribute or method that could belong to any car, rather than one that's specific
# to an electric car, should be added to the Car class instead of the ElectricCar class. Then
# anyone who uses the Car class will have that functionality available as well, and the
# ElectricCar class will only contain code for the information and behavior specific to
# electric car vehicles.
