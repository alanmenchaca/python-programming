"""A Dictionary of Similar Objects
You can also use a dictionary to store one kind of information about many objects"""

# Say you want to poll a number of people and ask them what their favorite programming
# language is.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
# Each key is the name of a person who responded to the poll, and each value is their
# language choice.

# To see which language Sarah chose, we ask for the value.
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

#  Looping through All Key-Value pairs
# If you loop through the favorite_languages dictionary, you get the name of each person
# in the dictionary and their favorite programming language. Because the keys always refer
# to a person's name and the value is always a language, we'll use the variables name and
# language in the loop instead of key and value.
print("\nLooping through All Key-Value pairs:")
for name, language in favorite_languages.items():
    print("\t- " + name.title() + "'s favorite language is " + language.title() + ".")
# Now, in just a few lines of code, we can display all of the information from the poll
# This type of looping would work just as well if our dictionary stored the results from
# polling a thousands or even a million people.

# Looping Through All the Keys in a Dictionary
# The keys method is useful when you don't need to work with all of the values in a dictionary.
print("\nNames:")
for name in favorite_languages.keys():
    print("* " + name.title())
# Looping through the keys is actually the default behavior when looping through a dictionary,
# so this code would have exactly the same output if we wrote:
# for name in favorite_language:

# We'll loop through the names in the dictionary as we did previously, but when the name matches
# one of our friends, we'll display a message about their favorite language.
print("\nLooping Through All the keys in a Dictionary:")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see you favorite language is "
              + favorite_languages[name].title() + "!")

# You can also use the keys() method to find out if a particular person was polled.
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!\n")

# Looping Through a Dictionary's Keys In Order
# One way to return items in a certain order is to sort the keys as they're returned in the for
# loop. You can use the sorted() function to get a copy of the keys in order.
for name in sorted(favorite_languages.keys()):
    # This tells Python to list all keys in the dictionary and sort that list before looping
    # through it.
    print(name.title() + ", thank you for taking the poll.")

# Looping Through All Values in a Dictionary
# If you are primarily interested in the values that a dictionary contains, you can use the values()
# method to return a list of values without any keys.
print("\nThe following languages have been mentioned:")
# The for statement here pulls each value from the dictionary and stores it in the variable language.
for language in set(favorite_languages.values()):
    # To see each language chosen without repetition, we can use a set. When we wrap set() around a list
    # that contains duplicate items, Python identifies the unique items in the list and builds a set
    # from those items.
    print("- " + language.title())
