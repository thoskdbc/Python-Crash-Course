# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:
# •If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# •Otherwise, print a generic greeting, such as Hello Jaden, thank you for
# logging in again.
usernames = ["tylor", "admin", "leo", "dani", "Jaden"]
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# •If the list is empty, print the message We need to find some users!
# •Remove all of the usernames from your list, and make sure the correct
# message is printed.
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")

# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# •Make a list of five or more usernames called current_users.
current_users = ["Thosk", "loktar", "FOX", "lonkat", "gumball"]
# •Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
new_users = ["frederik", "auron", "thosk", "dexter", "lonkat"]
# •Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} in not available, enter a new username")
    else:
        print(f"The username {new_user} is available")

# •Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
# current_users containing the lowercase versions of all existing users.)
print('\n')
lowercase_current_users = []
for user in current_users:
    lowercase_current_users.append(user.lower())

for new_user in new_users:
    if new_user in lowercase_current_users:
        print(f"{new_user} in not available, enter a new username")
    else:
        print(f"The username {new_user} is available")

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# •Store the numbers 1 through 9 in a list.
numbers = list(range(1, 10))
# •Loop through the list.
for number in numbers:
# •Use an if- elif- else chain inside the loop to print the proper ordinal end-
# ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
# 7th 8th 9th", and each result should be on a separate line.
    term = ""
    if number == 1:
        term = "st"
    elif number == 2:
        term = "nd"
    elif number == 3:
        term = "rd"
    else:
        term = "th"
        
    print(f"{number}{term}")