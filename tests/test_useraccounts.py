""" File to handle Unit Test for User accounts """
import unittest
from api.useraccounts import UserClass

class UserAccountsTestCases(unittest.TestCase):
    """ Users accounts tests case """

    def setUp(self):
        """ Setup Users Class test case """

        self.user = UserClass()

    def tearDown(self):
        """ Teardown Users Class test case  """

        del self.user

    def test_passwordLegth(self):
        """ Test to check if the user password has the desired length """

        msg = self.user.signupUser("chairman", "mochualex4@gmail.com", "qwerW", "qwerW")
        self.assertEqual(msg, "Input a password that is at least 8 characters long")

    def test_specialCharac(self):
        """ Test to check if the username has any special characters  """

        msg = self.user.signupUser("chairman$","mochualex4@gmail.com", "qwerWER4", "qwerWER4")
        self.assertIn("Username should not have special characters (. , ! space [])", msg)
    

    def test_invalidEmail(self):
        """ Test to check if the user entered an invalid email"""

        msg = self.user.signupUser("chairman", "mochualex4gmail.com", "qwerWER4", "qwerWER4")
        self.assertEqual(msg, "Please a provide a valid email")

    def test_passwordMismatch(self):
        """ Test to check if the users password are not matching"""

        msg = self.user.signupUser("chairman", "mochualex4@gmail.com", "wertrWER4", "qwerWER4")
        self.assertEqual(msg, "Password do not match")

    def test_existingUser(self):
        """ Test to check if their is an existing account of the user when signing up"""

        self.user.signupUser("chairman", "mochualex4@gmail.com", "wertrWER4", "wertrWER4")
        msg = self.user.signupUser("chairman", "mochualex4@gmail.com", "asdQWER4", "asdQWER4")
        self.assertIn("Account already exists. Please login or Recover account", msg)

    def test_correctInfo(self):
        """ Test to check if the user entered the correct info and registered successfully"""

        msg = self.user.signupUser("chairman", "mochualex4@gmail.com", "qwerWER4", "qwerWER4")
        self.assertEqual(msg, "Successfully created a weConnect Business Account. You can login!")