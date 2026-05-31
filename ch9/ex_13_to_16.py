# 9-13. Dice: Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll it
# 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
from random import randint
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

die1 = Die()
die2 = Die(10)
die3 = Die(20)
for i in range(1, 11):
    print(f"\n{i}_time:")
    die1.roll_die()
    die2.roll_die()
    die3.roll_die()



# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and
# five letters. Randomly select four numbers or letters from the list and print a
# message saying that any ticket matching these four numbers or letters wins a
# prize.
lottery_characters = [str(char) for char in range(1,11)] + ['a', 'z', 'k', 'p', 'g']
print("\nAny tickets matching these four numbers or letters wins something")


def pull_winner_ticket():
    winner_ticket = []

    for i in range(1, 5):
        index = randint(0, len(lottery_characters) - 1)
        char = lottery_characters[index]
        winner_ticket.append(char)

    print(f"Winner ticket: {winner_ticket}")
    return winner_ticket

winner_ticket = pull_winner_ticket()

# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
# the kind of lottery you just modeled. Make a list or tuple called my_ticket.
# Write a loop that keeps pulling numbers until your ticket wins. Print a message
# reporting how many times the loop had to run to give you a winning ticket.
my_ticket = ['7', '7', '7', '7']
winner_ticket = []
attempts = 0
while sorted(my_ticket) != sorted(winner_ticket):
    winner_ticket = pull_winner_ticket()
    attempts += 1

print(f"Attempts to get my ticket: {attempts}")



# 9-16. Python Module of the Week: One excellent resource for exploring the
# Python standard library is a site called Python Module of the Week. Go to
# https://pymotw.com/ and look at the table of contents. Find a module that
# looks interesting to you and read about it, perhaps starting with the random
# module.