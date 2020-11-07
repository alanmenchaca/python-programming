"""Copying a List
Often, you'll want to start with an existing list and make an entirely new list
based on the first one. To copy a list, you can make a slice that includes the
entire original list by omitting the first index and the second index ([:])"""

my_foods = ['pizza', 'falafel', 'carrot cake']
# This tells Python to make a slice that starts at the first item and ends with
# the last item, producing a copy of the entire list.
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy Friend's favorite foods are:")
print(friend_foods)

# This doesn't work.
# friend_foods = my_foods