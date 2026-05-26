# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the
# values that are returned.
def city_country(city, country):
    formatted_string = f"{city.title()}, {country.title()}"
    return formatted_string

print(city_country('buenos aires', 'argentina'))
print(city_country('la paz', 'bolivia'))
print(city_country('lima', 'peru'))



# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.
def make_album(artist, album, songs=None):
    music_album = {
        'artist': artist,
        'album': album
    }
    if songs:
        music_album['songs'] = songs
    return music_album

print(make_album('michael jackson', 'thriller'))
print(make_album('pink floyd', 'the dark side of the moon'))
print(make_album('fleetwood mac', 'rumours'))
print(make_album('prince', 'purple rain', 5))



# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.
print("Enter information about your favorite artists and albums:\n"
      "(Enter 'q' any time to quit)")
while True:
    artist = input("Enter artist: ")
    if artist == 'q':
        break
    album = input("Enter album: ")
    if album == 'q':
        break
    songs = input("Enter number of songs: ")
    if songs == 'q':
        break

    print(make_album(artist, album, songs))
