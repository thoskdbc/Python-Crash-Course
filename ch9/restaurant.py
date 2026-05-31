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
