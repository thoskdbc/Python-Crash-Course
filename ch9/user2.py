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