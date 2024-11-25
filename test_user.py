import unittest
from user import User

class MockDependency:
    def action(self):
        return "Mocked Action"

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(1, "test_user", "test@example.com")
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.email, "test@example.com")

    def test_get_user_info(self):
        user = User(2, "another_user", "another@example.com")
        user_info = user.get_user_info()
        self.assertEqual(user_info["user_id"], 2)
        self.assertEqual(user_info["username"], "another_user")
        self.assertEqual(user_info["email"], "another@example.com")

    def test_dependency_injection(self):
        mock_dependency = MockDependency()
        user = User(1, "test_user", "test@example.com", dependency=mock_dependency)
        self.assertEqual(user.do_something(), "Mocked Action")

    def test_no_dependency(self):
        user = User(1, "test_user", "test@example.com")
        self.assertEqual(user.do_something(), "No dependency provided")

if __name__ == "__main__":
    unittest.main()
