# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.
person0 = {
    'first_name': 'robert',
    'last_name': 'vargas',
    'age': 21,
    'city': 'paris'
}
person1 = {
    'first_name': 'claudia',
    'last_name': 'cheimbau', # xd
    'age': 65,
    'city': 'mexico',
}
person2 = {
    'first_name': 'billie',
    'last_name': 'eilish',
    'age': 24,
    'city': 'united states',
}
people = [person0, person1, person2]
for person in people:
    print("\nPerson:")
    for field, data in person.items():
        if field == 'age':
            print(f"{field.title()}: {data}")
        else:
            print(f"{field.title()}: {data.title()}")



# 6-8. Pets: Make several dictionaries, where each dictionary represents a differ-
# ent pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.
pets = [
    {
        'kind': 'dog',
        'owner': 'ronald',
    },
    {
        'kind': 'cat',
        'owner': 'rebeca',
    },
    {
        'kind': 'fish',
        'owner': 'robert',
    }
]
for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['kind']}")



# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.
favorite_places = {
    'diana': 'zurishe',
    'paul': 'tokio',
    'dane': 'paris',
}
for name, place in favorite_places.items():
    print(f"{name.title()}'s favorite place is {place.title()}")



# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
# so each person can have more than one favorite number. Then print each per-
# son’s name along with their favorite numbers.
favorite_numbers = {
    'luz': [7, 65, 99],
    'carolina': [70, 80],
    'raven': [100, 20, 11, 2],
}
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")



# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the infor-
# mation you have stored about it.
cities = {
    'barcelona': {
        'country': 'spain',
        'population': "50 million",
        'fact': "it is the world's leading producer of olive oil",
    },
    'cochabamba': {
        'country': 'bolivia',
        'population': "13 million",
        'fact': "it is a landlocked nation in central South America",
    },
    'berlin': {
        'country': 'germany',
        'population': "85 million",
        'fact': "it is the most populous member state of the European Union",
    },
}
for city, info in cities.items():
    print(f"\nInformation about {city.title()}:")
    for field, data in info.items():
        print(f"{field.title()}: {data.capitalize()}")



# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example pro-
# grams from this chapter, and extend it by adding new keys and values, chang-
# ing the context of the program or improving the formatting of the output.
# many_users.py
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'hobbies': ["sailing", "hiking", "play music"],
        'profession': "theoretical physicist",
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'profession': "chemist",
        'hobbies': ["cycling", "mountaineering", "swimming"],
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    for field, data in user_info.items():
        if field == "hobbies":
            print(f"Hobbies:")
            for hobbie in data:
                print(f"\t{hobbie.title()}")
        else:
            print(f"{field.title()}: {data.title()}")
    