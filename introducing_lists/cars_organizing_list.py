"""Organizing list
Often, your introducing_lists will be created in an unpredictable order, because you can't always
 control the order in which your users provide their data."""

# Sorting a List Permanently with the sort() Method
# The sort() method, changes the order of the list permanently.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("In normal order: " + str(cars))

# The cars are now in alphabetical order, and we can never revert to the original order.
cars.sort()
print("In alphabetical order: " + str(cars))

# You can also sort this list in reverse alphabetical order by passing the argument
# reverse=True to the sort() method.
cars.sort(reverse=True)
# The order of the list is permanently changed
print(cars)

# Sorting a List Temporarily with the sorted() Function
# The sorted() function lets you display your list in a particular order but doesn't
# affect the actual order of the list.
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Printing a List in Reverse Order
# To reverse the original order of a list, you can use the reverse() method.
# Notice that reverse() doesn't sort backward alphabetically; it simply
# reverses the order of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print("\nThe list in reverse order: " + str(cars))
# The reverse() method changes the order of a list permanently, but you can revert to
# the original order anytime by applying reverse() to the same list a second time.

# Finding the Length of a List
# You can quickly find the length of a list by using the len() function
cars_length = len(cars)
print("Cars Length: " + str(cars_length))
