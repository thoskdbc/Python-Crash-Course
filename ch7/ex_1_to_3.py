# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”
car = input("what kind of rental car you would like? ")
print(f"Let me see if I can find you a {car.capitalize()}.")



# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message say-
# ing they’ll have to wait for a table. Otherwise, report that their table is ready.
number_of_people = input("how many people are in your dinner group? ")
number_of_people = int (number_of_people)
if number_of_people > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")



# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.
number = int(input("Enter a number to see if it's multiple of ten: "))
if number % 10 == 0:
    print(f"The number {number} is multiple of ten")
else:
    print(f"The number {number} isn't multiple of ten")