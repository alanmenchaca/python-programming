"""Checking Whether a Value is Not in a List
Other times, it's important to know if a value does not appear in a list.
You can use the keyword not in this situation. For example, consider a list of users who
are banned from commenting in a forum. You can check whether a user has been banned before
allowing that person to submit a comment."""

banned_users = ['andre', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
# If the value of user is not in the list banned_users, Python returns a True and
# executes the idented line.


