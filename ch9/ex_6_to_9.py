from ex_4_to_5 import Restaurant, User
# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors=[]):
        """Initialize the IcecreamStand atributes and adds flavors"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors


    def show_flavors(self):
        """Prints the list of flavors"""
        print("List of flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream_stand = IceCreamStand("cold", "Italian", ['chocolate', 'vanilla'])
ice_cream_stand.show_flavors()



# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.
class Privileges:
    """This class is on charge of privileges"""
    def __init__(self):
        """Initialice the privileges by default"""
        self.privileges = ["can add post", "can delete post", "can ban user"]


    def show_privileges(self):
        """Show the privileges"""
        print("Showing privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.
class Admin(User):
    """A simple attempt to represent an admin"""
    def __init__(self, first_name, last_name, **extra_data):
        """Initialize the privileges"""
        super().__init__(first_name, last_name, **extra_data)
        # self.privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = Privileges()

    # def show_privileges(self):
    #     """Show the privileges"""
    #     print("Showing privileges:")
    #     for privilege in self.privileges:
    #         print(f"- {privilege}")

admin = Admin('brad', 'pitt')
admin.privileges.show_privileges()

    

# Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 100 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and
# then call get_range() a second time after upgrading the battery. You should
# see an increase in the car’s range.
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):
        self.odometer_reading += miles



class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
           range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


    def upgrade_battery(self):
        """Upgrades the battery size"""
        if self.battery_size < 100:
            self.battery_size = 100



class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()



electric_car = ElectricCar('tesla', 'v2', '2020')
electric_car.battery.get_range()
electric_car.battery.upgrade_battery()
electric_car.battery.get_range()