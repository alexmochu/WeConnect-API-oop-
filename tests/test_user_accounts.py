""" File to handle Unit Test for User accounts """
import unittest
from api.user_accounts import UserClass

class TestUserAccountsTestCases(unittest.TestCase):
    """ Users accounts tests case """

    def setUp(self):
        """ Setup Users Class test case """

        self.user = UserClass()

    def test_password_length(self):
        """ Test to check if the user password has the desired length """

        msg = self.user.register("chairman", "mochualex4@gmail.com", "qwerW", "qwerW")
        self.assertEqual(msg, "Input a password that is at least 8 characters long")

    # Testisng User registration
    def test_special_characters(self):
        """ Test to check if the username has any special characters  """

        msg = self.user.register("chairman$", "mochualex4@gmail.com", "qwerWER4", "qwerWER4")
        self.assertIn("Username should not have special characters (. , ! space [])", msg)

    def test_invalid_email(self):
        """ Test to check if the user entered an invalid email"""

        msg = self.user.register("chairman", "mochualex4gmail.com", "qwerWER4", "qwerWER4")
        self.assertEqual(msg, "Please a provide a valid email")

    def test_password_mismatch(self):
        """ Test to check if the users password are not matching"""

        msg = self.user.register("chairman", "mochualex4@gmail.com", "wertrWER4", "qwerWER4")
        self.assertEqual(msg, "Password do not match")

    def test_existing_user(self):
        """ Test to check if their is an existing account of the user when signing up"""

        self.user.register("chairman", "mochualex4@gmail.com", "wertrWER4", "wertrWER4")
        msg = self.user.register("chairman", "mochualex4@gmail.com", "asdQWER4", "asdQWER4")
        self.assertIn("Account already exists. Please login or Recover account", msg)

    def test_correct_info(self):
        """ Test to check if the user entered the correct info and registered successfully"""

        msg = self.user.register("chairman", "mochualex4@gmail.com", "qwerWER4", "qwerWER4")
        self.assertEqual(msg, "Successfully created a weConnect Business Account. You can login!")

    # Testing Login
    def test_if_user_is_registered(self):
        """ Checking if the user has an account """

        self.user.users_list = [{'username': 'chairman', 'password': 'qwerWER4', 'email': 'mochualex4@gmail.com'}]
        msg = self.user.login("Dolf", "qwerWER4")
        self.assertEqual(msg, "You have no account,please sign up")

    def test_login_wrong_password(self):
        """ Checking if user log in with wrong password """

        self.user.users_list = [{'username': 'chairman', 'password': 'qwerWER4', 'email': 'mochualex4@gmail.com'}]
        msg = self.user.login("chairman", "asdQWER34")
        self.assertEqual(msg, "Incorrect password")

    def test_correct_login(self):
        """ Checking if user login with correct credentials or successfully """

        self.user.users_list = [{'username': 'chairman', 'password': 'qwerWER4', 'email': 'mochualex4@gmail.com'}]
        msg = self.user.login("chairman", "qwerWER4")
        self.assertIn("Successfully logged in to weConnect API. Create a Business page!", msg)

    def tearDown(self):
        """ Teardown Users Class test case  """

        del self.user

if __name__ == '__main__':
    unittest.main()