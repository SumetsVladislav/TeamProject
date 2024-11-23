from interfaces import IUser

class User(IUser):
    def get_user_info(self) -> dict:
        return {"name": "Alice", "email": "alice@example.com"}
