# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# •Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points.
# •Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)
alien_color = 'green'
if alien_color.lower() == 'green':
    print("You just earned 5 points\n")

# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
# write an if- else chain.
# •If the alien’s color is green, print a statement that the player just earned
# 5 points for shooting the alien.
# •If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.
# •Write one version of this program that runs the if block and another that
# runs the else block.
alien_color = 'red'
if alien_color.lower() == 'green':
    print("You just earned 5 points")
else:
    print("You just earned 10 points")

# 5-5. Alien Colors #3: Turn your if- else chain from Exercise 5-4 into an if- elif-
# else chain.
# •If the alien is green, print a message that the player earned 5 points.
# •If the alien is yellow, print a message that the player earned 10 points.
# •If the alien is red, print a message that the player earned 15 points.
# •Write three versions of this program, making sure each message is printed
# for the appropriate color alien.
points = 0
alien_color = 'yellow'

if alien_color.lower() == 'green':
    points = 5
elif alien_color.lower() == 'yellow':
    points = 10
else:
    points = 15

print(f"You just earned {points} points")

# 5-6. Stages of Life: Write an if- elif- else chain that determines a person’s
# stage of life. Set a value for the variable age, and then:
age = 66
stage = ''
# •If the person is less than 2 years old, print a message that the person is
# a baby.
if age < 2:
    stage = 'baby'
# •If the person is at least 2 years old but less than 4, print a message that
# the person is a toddler.
elif age < 4:
    stage = 'toddler'
# •If the person is at least 4 years old but less than 13, print a message that
# the person is a kid.
elif age < 13:
    stage = 'kid'
# •If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager.
elif age < 20:
    stage = 'teenager'
# •If the person is at least 20 years old but less than 65, print a message that
# the person is an adult.
elif age < 65:
    stage = 'adult'
# •If the person is age 65 or older, print a message that the person is an
# elder.
else:
    stage = 'elder'

print(f"The person is a/an {stage}")

# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list.
# •Make a list of your three favorite fruits and call it favorite_fruits.
# •Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!
fruits = ["watermelon", "strawberry", "cherry", "pineapple", "kiwi"]
fruit = 'papaya'
if fruit in fruits:
    print(f"{fruit} is in the list")
fruit = 'cherry'
if fruit in fruits:
    print(f"{fruit} is in the list")

favorite_frutes = ['apple', 'banana', 'grapes']
fruit = "banana"
if fruit in favorite_frutes:
    print(f"You really like {fruit}!")
fruit = "kiwi"
if fruit in favorite_frutes:
    print(f"You really like {fruit}!")
fruit = "apple"
if fruit in favorite_frutes:
    print(f"You really like {fruit}!")
fruit = "orange"
if fruit in favorite_frutes:
    print(f"You really like {fruit}!")
fruit = "grapes"
if fruit in favorite_frutes:
    print(f"You really like {fruit}!")