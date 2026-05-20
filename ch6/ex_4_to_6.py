# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.
from ex_1_to_3 import glossary
print('\n')
for word, concept in glossary.items():
    print(f"{word}: {concept}")

glossary['dictionary'] = "a collection of key-value pairs where keys are used to access values"
glossary['bug'] = "an unintended error or flaw in a program"
glossary['format'] = "the way data is represented or organized"
glossary['print'] = "a function that displays data in the console"
glossary['set'] = "a collection of unique items used for mathematical operations"

for word, concept in glossary.items():
    print(f"{word}: {concept}")



# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
major_rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': "united states",
}

# •Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
for river, country in major_rivers.items():
    print(f"The {river} runs through {country}.")

# •Use a loop to print the name of each river included in the dictionary.
for river in major_rivers.keys():
    print(river)

# •Use a loop to print the name of each country included in the dictionary.
for country in major_rivers.values():
    print(country)



# 6-6. Polling: Use the code in favorite_languages.py (page 97).
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# •Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
people_who_should = ["max", "phil", "sarah", "rudy"]
# •Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.
people_who_taken = favorite_languages.keys()
for person in people_who_should:
    if person in people_who_taken:
        print(f"Thank you, {person.title()}, for taking the poll")
    else:
        print(f"{person.title()}, you should take the poll")
