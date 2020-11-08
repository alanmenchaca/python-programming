"""When we loop through the dictionary, the value associated with each person
would be a list of languages rather than a single language.
Inside the dictionary's for loop, we use another for loop to run through the
list of languages associated with each person."""

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

# When we loop through the dictionary, we use the variable name languages to hold
# each value from the dictionary, because we know that each value will be a list.
# Inside the main dictionary loop, we use another for loop to run through each
# person's list of favorite languages.
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")

    for language in languages:
        print("\t" + language.title())
# You should not nest lists and dictionaries to deeply. If you're nesting items much
# deeper than what you see in the preceding examples or you're working with someone
# else's code with significant levels of nesting, most likely a simpler way to solve
# the problem exists.
