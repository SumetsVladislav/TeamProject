from interfaces import IUser

class User(IUser):
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def get_user_info(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
        }

    def new_method(self):
        return "This is a new method"
	

# Зміна розробника для демонстрації stash
