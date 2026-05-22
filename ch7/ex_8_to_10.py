# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari-
# ous sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.
sandwich_orders = ['tuna', 'salmon', 'chicken', 'pork']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print("Sandwiches ready to serve:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.
sandwich_orders = ['tuna', 'pastrami', 'salmon', 'chicken', 'pastrami', 'pork', 'pastrami']
finished_sandwiches = []
print("The deli has run out of pastrami")

sandwich = 'pastrami'
while sandwich in sandwich_orders:
    sandwich_orders.remove(sandwich)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)



# 7-10. Dream Vacation: Write a program that polls users about their dream vaca-
# tion. Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.
vacation_poll = {}
polling_active = True
while polling_active:
    name = input("Hello, what's your name? ")
    place = input(f"{name.title()}, if you could visit one place in the world, "
                    "where would you go? ")
    vacation_poll[name] = place

    repeat = input("Would you like to repeat the poll? [Y/n] ")
    polling_active = repeat != 'n'

for name, place in vacation_poll.items():
    print(f"{name}: {place}")