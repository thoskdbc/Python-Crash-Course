# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.
person = {
    'first_name': 'robert',
    'last_name': 'vargas',
    'age': 21,
    'city': 'paris'
}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.
names = ['alex', 'toni', 'robin', 'gabi', 'thomas']
favorite_number = {
    'alex': 8,
    'toni': 3,
    'robin': 4,
    'gabi': 9,
    'thomas': 6,
}
for name in names:
    print(f"{name.title()} favorite number: {favorite_number[name]}")

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# •Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# •Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.
words = ['variable', 'input', 'output', 'loop', 'boolean', 'bug']
glossary = {
    'variable': "a reserved section in memory with a name to be refered to.",
    'input': "data received in order to make a computation.",
    'output': "a result of data being computed or data being displayed.",
    'loop': "a finite repetition of something like an instruction.",
    'boolean': "a type of value that have only two possible values, true or false."
}
for word in words:
    print(f"{word.title()}: {glossary.get(word, "the glossary doesn't have information")}")