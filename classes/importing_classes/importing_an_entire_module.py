"""Importing an Entire Module
You can also import an entire module and then access the classes you need using dot
notation. This approach is simple and results in code that is easy to read. Because
every call that creates an instance of a class includes the module name, you won't
have naming conflicts with any names used in the current file."""
import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
my_tesla = car.ElectricCar('tesla', 'roadster', 2016)

# Importing All Classes from a Module
# You can import every class from a module using the following syntax.
# from module_name import *
# This method is no recommended for two reasons. First, it's helpful to be able to read the
# import statements at the top of a file and get a clear sense of which classes a program
# uses. Whit this approach it's unclear which classes you're using from the module. This
# approach can also lead to confusion with names in the file. If you need to import many
# classes from a module, you're better off importing the entire module and using the
# module_name.class_name syntax. You won't see all the classes used at the top of the file,
# but you'll see clearly where the module is used in the program.
