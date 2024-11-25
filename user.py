from interfaces import IUser

class User(IUser):
    def __init__(self, user_id, username, email, dependency=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.dependency = dependency  # Нове поле для впровадження залежностей

    def get_user_info(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
        }

    def do_something(self):
        if self.dependency:
            return self.dependency.action()
        else:
            return "No dependency provided"

