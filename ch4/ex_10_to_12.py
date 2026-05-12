# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
shows = ["mr_robot", "invincible", "twd", "mandalorian", "dexter"]
print(shows)

# •Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
print("The first three items in the list are:")
for show in shows[:3]:
    print(show)

# •Print the message Three items from the middle of the list are:. Use a slice to
# print three items from the middle of the list.
print("Three items from the middle of the list are:")
mid_index = len(shows) // 2
for show in shows[(mid_index - 1):(mid_index + 2)]:
    print(show)

# •Print the message The last three items in the list are:. Use a slice to print the
# last three items in the list.
print("The last three items in the list are:")
print(shows[-3:])

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
import ex_1_to_2
my_pizzas = ex_1_to_2.pizzas
friend_pizzas = my_pizzas[:]

# •Add a new pizza to the original list.
my_pizzas.append("berlin")

# •Add a different pizza to the list friend_pizzas.
friend_pizzas.append("german")

# •Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the sec-
# ond list. Make sure each new pizza is stored in the appropriate list.
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
    
# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)