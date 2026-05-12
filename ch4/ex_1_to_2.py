# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
pizzas = ["classic", "hawayan", "paris"]
for pizza in pizzas:
    print(pizza.title())
print()
# •Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza.")
# •Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!
print("I really love pizza!\n")
# 4-2. Animals: Think of at least three different animals that have a common char-
# acteristic. Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.
animals = ["monkey", "elephat", "lion"]
# •Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
for animal in animals:
    print("A", animal, "is a wild animal")
# •Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!
print("These animals wouldn't be a great pet")