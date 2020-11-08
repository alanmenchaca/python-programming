from collections import OrderedDict

# Dictionaries allow you to connect pieces of information, but the don't keep track of the
# order in which you add key-value pairs. If you're creating a dictionary and want to keep
# track of the order in which key-value pairs are added, you can use the OrderedDict class
# from the collections module. Instances of the OrderedDict class behave almost exactly like
# dictionaries except the keep track of the order in which key-value pairs are added.
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

# This is a great class to be aware of because it combines the main benefit of lists (retaining
# your original order) with the main feature of dictionaries (connecting pieces of information).
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
