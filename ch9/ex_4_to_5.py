# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any num-
# ber you like that could represent how many customers were served in, say, a
# day of business.
class Restaurant:
    """
        Simulates a restaurant with name and cuisine type
        Modified: store the number served and related methods
    """
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0


    def describe_restaurant(self):
        print(f"The restaurant name is: {self.restaurant_name}\n"
              f"The cuisine type is: {self.cuisine_type}")


    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")


    def get_number_served(self):
        print(self.number_served)


    def set_number_serverd(self, number_served):
        self.number_served = number_served


    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant("rost and roll", "american")

restaurant.get_number_served()
restaurant.number_served = 10
restaurant.get_number_served()
restaurant.set_number_serverd(15)
restaurant.get_number_served()
restaurant.increment_number_served(5)
restaurant.get_number_served()



# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called increment_login
# _attempts() that increments the value of login_attempts by 1. Write another
# method called reset_login_attempts() that resets the value of login_attempts
# to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.
class User:
    """
        Models a user with first name, last name and if extra data is entered, it also
        stores it
        Modified: store login attemps and related methods
    """
    def __init__(self, first_name, last_name, **extra_data):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.extra_data = extra_data
        self.login_attempts = 0


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


    def get_login_attempts(self):
        print(self.login_attempts)


    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("mark", "grayson")
user.get_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.get_login_attempts()
user.reset_login_attempts()
user.get_login_attempts()