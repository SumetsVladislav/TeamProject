from user import User

def test_user():
    user = User()
    info = user.get_user_info()
    assert info["name"] == "Alice", "Ім'я не відповідає очікуваному"
    assert info["email"] == "alice@example.com", "Email не відповідає очікуваному"
    print("All tests passed successfully")

if __name__ == "__main__":
    test_user()

