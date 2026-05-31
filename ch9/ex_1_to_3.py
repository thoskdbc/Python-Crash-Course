# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()


    def describe_restaurant(self):
        print(f"The restaurant name is: {self.restaurant_name}\n"
              f"The cuisine type is: {self.cuisine_type}")


    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

restaurant = Restaurant("kfc", "american")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()



# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.
restaurant1 = Restaurant("chicken's kingdom", "bolivian")
restaurant2 = Restaurant("La Cantonata", "european")
restaurant3 = Restaurant("La Estancia", "Latin cuisine")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()



# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.
class User:
    """
        Models a user with first name, last name and if extra data is entered, it also
        stores it
    """
    def __init__(self, first_name, last_name, **extra_data):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.extra_data = extra_data


    def describe_user(self):
        print("User data summary:")
        print(f"First Name: {self.first_name}\n"
              f"Last Name: {self.last_name}")
        
        for field, data in self.extra_data.items():
            # The type function returns the type of a value
            if type(data) == str:
                print(f"{field.title()}: {data.title()}")
            else:
                print(f"{field.title()}: {data}")

    
    def greet_user(self):
        complete_name = self.first_name + ' ' + self.last_name
        print(f"Good morning, {complete_name}")

user1 = User("robert", "becker", age=23, nickname='robeck')
user2 = User("tony", "gambino", location='italy', active=True)
user3 = User("thomas", "vargas")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()