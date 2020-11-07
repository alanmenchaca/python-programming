"""Using a while loop with Lists and Dictionaries
A for loop is effective for looping through a list, but you shouldn't modify
a list inside a for loop because Python wil have trouble keeping track of the
items in the list. To modify a list as you work through it, use a while loop.
Using while loops with lists and dictionaries allows you to collect, store,
and organize lots of input to examine and report on later."""

# Moving Items from One List to Another
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    # When the list of unconfirmed users is empty, the loop stops and the list of
    # confirmed users is printed.
    current_user = unconfirmed_users.pop()

    print("Verifying user: %s" % current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print("- %s" % confirmed_user.title())

# We simulate confirming each user by printing a verification message and then
# adding them to the list of confirmed users. As the list of unconfirmed users
# shrinks, the list of unconfirmed users grows.
