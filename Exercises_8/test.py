import unittest

from conditions import User

positive_user_data = {'login': 'tanderson', 'password': 'tanderson123', 'first_name': 'Thomas', 'last_name': 'Anderson',
                      'id': '123', 'address': '1234', 'city': 'Krakow', 'company_name': 'DA',
                      'current_status': 'available',
                      'email': 'aaaa@gmail.com'}
negative_user_data = {
    'login': 'asmith', 'password': 'asmith123', 'first_name': 'Agent', 'last_name': 'Smith', 'id': '321',
    'address': '4321', 'city': 'Wroclaw', 'company_name': 'GD', 'current_status': 'unavailable',
    'email': 'bbbb@gmail.com'}


class TestUser(unittest.TestCase):
    user = User(positive_user_data['login'], positive_user_data['password'], positive_user_data['first_name'],
                positive_user_data['last_name'])

    def test_user_has_correct_data(self):
        """
        Test that user has correct data after creating
        """
        for prop_key in list(self.user.__dict__.keys()):
            with self.subTest(f"Should be User has correct {prop_key}"):
                self.assertEqual(getattr(self.user, prop_key), positive_user_data[f'{prop_key}'])

    def test_user_has_not_incorrect_data(self):
        """
        Test that user hasn't incorrect data after creating
        """
        for prop_key in list(self.user.__dict__.keys()):
            with self.subTest(f"Should be User hasn't incorrect {prop_key}"):
                self.assertNotEqual(getattr(self.user, prop_key), negative_user_data[f'{prop_key}'])


if __name__ == '__main__':
    unittest.main()
