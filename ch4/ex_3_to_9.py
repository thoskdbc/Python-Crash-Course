# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.
print("Numbers from 1 to 20")
for number in range(1, 21):
    print(number)
# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)
numbers = list(range(1, 1000001))
print("Numbers from 1 to 1000000")
for number in numbers:
    print(number)
# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.
minimum = min(numbers)
maximun = max(numbers)
summation = sum(numbers)
print(f"\nMinimum: {minimum}\nMaximum: {maximun}\nSummation: {summation}\n")
# 4-6. Odd Numbers: Use the third argument of the range() function to make a
# list of the odd numbers from 1 to 20. Use a for loop to print each number.
odd_numbers = []
for odd in range(1, 21, 2):
    odd_numbers.append(odd)
print("Odd numbers from 1 to 20")
for odd in odd_numbers:
    print(odd)
# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
mult_of_three = list(range(3, 31, 3))
print("Multiples of 3, from 3 to 30")
for mult in mult_of_three:
    print(mult)
# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.
print("Cubes from 1 to 10:")
cubes = []
for num in range(1, 11):
    cubes.append(num ** 3)
for cube in cubes:
    print(cube)
# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.
print("Cubes by list comprenhension")
cubes_c = [value ** 3 for value in range(1, 11)]
for cube_c in cubes_c:
    print(cube_c)