from user import User
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



class Admin(User):
    """A simple attempt to represent an admin"""
    def __init__(self, first_name, last_name, **extra_data):
        """Initialize the privileges"""
        super().__init__(first_name, last_name, **extra_data)
        # self.privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = Privileges()