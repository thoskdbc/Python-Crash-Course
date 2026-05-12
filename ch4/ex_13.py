# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
basic_foods = ("chicken", "hamburger", "potato", "tomato", "noodle")
# •Use a for loop to print each food the restaurant offers.
for food in basic_foods:
    print(food)
# •Try to modify one of the items, and make sure that Python rejects the
# change.
# basic_foods[0] = "rice" -> was rejected
# •The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.
basic_foods = ("chicken", "rice", "potato", "tomato", "bread")
for food in basic_foods:
    print(food)
print(basic_foods[2:])