"""Using Arbitrary Keyword Arguments
Sometimes you'll want to accept an arbitrary number of arguments, but you won't
know ahead of time what kind of information will be passed to the function. In this
case, you can write functions that accept as many key-value pairs as the calling
statement provides."""


# The definition of build_profile() expects a first and last name, and then it allows
# the user to pass in as many name-value pairs as they want. The double asterisks before
# the parameter **user_info cause Python to create an empty dictionary called user_info
# and pack whatever name-value pairs ot receives into this dictionary.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile


# You can mix positional, keyword, and arbitrary values in many different ways when writing
# your own functions. The returned dictionary contains the user's first and last names and,
# in this case, the location and field of study as well. The function would work no matter
# how many additional key-value pairs are provided in the function call.
user_profile = build_profile('albert', 'einstein',
                             location='princeton', field='physics')
# We call build_profile(), passing it the first name 'albert', the last name 'einstein', and
# the two key-value pairs location='princeton' and field='physics'. We store the returned
# profile in user_profile.

print(user_profile)
