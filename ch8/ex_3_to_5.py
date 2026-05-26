# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.
def make_shirt(size, message):
    """Prints details of a shirt"""
    print(f"The size of the shirt is: {size.title()}\n"
          f"The message printed on it is: {message.upper()}")

make_shirt('m', "freedom")
make_shirt(size='l', message="saints")



# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.
def make_shirt(size='L', message="I love Python"):
    """Prints details of a shirt but has default values"""
    print(f"The size of the shirt is: {size.title()}\n"
          f"The message printed on it is: {message.upper()}")

make_shirt()
make_shirt(size='m')
make_shirt('s', "hello world")



# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.
def describe_city(city, country='somewhere'):
    """Describes the country of a city"""
    print(f"{city.title()} is in {country.title()}")

describe_city('paris', 'france')
describe_city('tokio', 'japan')
describe_city('murcia')