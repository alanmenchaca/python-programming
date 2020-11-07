"""Changing, Adding, and Removing Elements
Most introducing_lists you create will be dynamic, meaning you'll build a list and then add
and remove elements from it as your program runs its course."""

# Modifying elements in a List
# To change an element in a List, use the name of the list followed by the index
# of the element you want to change, and then provide the new value you want that
# item to have.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles[0] = 'honda'
# Appending Elements to the End of a List
# The simplest way to add a new elements to a list is to append the item to the list
# When you append an item to a list, the new element is added to the end of the list.
print("The new element is added to the end of the list.")
motorcycles.append('ducati')

# The append() method makes it easy to build introducing_lists dynamically.
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Inserting Elements into a List
# You can add a new element at any position in your list by using the insert() method
motorcycles.insert(0, 'ducati')
# The insert() method opens a space at position 0 and stores the value 'ducati' at that location.
print(motorcycles)

# Removing an Item Using the del Statement
# If you know the position of the item you want to remove from a list, you can use the del statement.
del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method
# The pop method removes the last item in a list, but it lets you work with that item after removing
# it. The term pop comes from thinking of a list as a stack of items and popping one item off the top
# of the stack.
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print("popped_motorcycle: {}".format(popped_motorcycle))

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a {}.".format(last_owned.title()))

# Popping Items from any Position in a List
# You can actually use pop() to remove an item in a list at any position by including the index of the
# item you want to remove in parentheses.
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a {}.'.format(first_owned.title()))
# When you want to delete an item from a list and not use that element item in any way, use the del
# statement; if you want to use an item as you remove it, use the pop() method.

# Removing item by value
# If you only know the value of the item you want to remove, you can use the remove() method.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
# ------------------------------------------------------------------------------------------------

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print("\n" + str(motorcycles))

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA {} is too expensive for me".format(too_expensive))




