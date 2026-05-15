# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
name = 'Thomas'
print("Is name == 'Thomas'? I predict True.")
print(name.lower() == 'thomas') # and so on...
# •Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# •Create at least ten tests. Have at least five tests evaluate to True and
# another five tests evaluate to False.
country = 'Spain'
movie = 'StarWars'
print(country.lower() == 'spain')
print(country == 'spain')
print(movie.lower() == 'starwars')
print(movie == 'starwars') # so on...
# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to ten. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
# •Tests for equality and inequality with strings
string1 = 'Hello'
string2 = 'Word'
print(string1 == string2)
print(string1 != string2)
# •Tests using the lower() method
print(string1.lower() == 'hello')
print(string1.lower() != 'hello')
# •Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
num1 = 3
num2 = 5
print(f"{num1} = {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} >= {num2}: {num1 >= num2}")
print(f"{num1} <= {num2}: {num1 <= num2}")
# •Tests using the and keyword and the or keyword
odd1 = 1
odd2 = 6
print(f"are {odd1} and {odd2} both odd numbers?")
print((odd1 % 2) != 0 and (odd2 % 2) != 0)
print(f"is {odd1} or {odd2} odd?")
print((odd1 % 2) != 0 or (odd2 % 2) != 0)
# •Test whether an item is in a list
items = [3, 'a', "hello"]
item = 'b'
print(item in items)
# •Test whether an item is not in a list
print(item not in items)