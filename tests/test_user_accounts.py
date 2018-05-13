""" Fileunittest to handle Unit Test for User accounts """
import os
import unittest
import tempfile

from flask import json, jsonify
# local import
from api.views import app
from api.user_accounts import UserClass

class TestUserAccountsTestCases(unittest.TestCase):
    """ Users accounts tests case """

    def setUp(self):
        """ Setup Users Class test case """
        app.testing = True
        self.app = app.test_client()
        self.data = {"email":"mochualex4@gmail.com", "username":"chairman", "password":"qweR12#$", "confirm_password":"qweR12#$"}
        self.data1 = {"email":"mochualex41@gmail.com", "username":"chairman1", "password":"qweR12#$", "confirm_password":"qweR12#$"}
        self.data2 = {"email":"mochualex41@gmail.com", "username":"chairman1", "password":"qwe", "confirm_password":"qwe"}
        self.data3 = {"email":"mochualex42@gmail.com", "username":"chair&*man1", "password":"qweR12#$", "confirm_password":"qweR12#$"}
        self.data4 = {"email":"mochualex43@gmail.com", "username":"chairman3", "password":"qwertyuui", "confirm_password":"qwertyuui"}
        self.data5 = {"email":"mochualex44@gmail.com", "username":"cha", "password":"qweR12#$", "confirm_password":"qweR12#$"}
        self.data6 = {"email":"mochualex44gmail.com", "username":"chairman4", "password":"qweR12#$", "confirm_password":"qweR12#$"}
        self.data7 = {"email":"mochualex45@gmail.com", "username":"chairman5", "password":"qweR12#$", "confirm_password":"qwejkR12#$"}
        self.data8 = {"email":"mochualex4@gmail.com", "username":"chairman", "password":"qweR12#$w", "confirm_password":"qweR12#$"}
        self.data9 = {"email":"mochualex46@gmail.com", "username":"chairman6", "password":"qweR12#$", "confirm_password":"qweR12#$"}
        self.data10 = {"new_password": "tn&T4tyY", "confirm_password": "tn&T4tyY"}
        self.data11 = {"new_password": "tn&T4tyyY", "confirm_password": "tn&T4tyY"}

        self.app.post('/api/v1/auth/register', data=json.dumps(self.data), content_type='application/json')

    def test_duplicate_register(self):
        """ check duplicate registeration view """
        response1 = self.app.post('/api/v1/auth/register', data = json.dumps(self.data) , content_type = 'application/json')
        result1 = json.loads(response1.data.decode())
        self.assertEqual(result1["message"], "Account already exists. Please login or Recover account")

    def test_register_user(self):
        """ check registered user view """
        response = self.app.post('/api/v1/auth/register', data = json.dumps(self.data1) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Successfully created a weConnect Business Account. You can login!")
        self.assertEqual(response.status_code, 201)

    def test_password_length(self):
        """ Test to check if the user password has the desired length """
        response = self.app.post('/api/v1/auth/register', data = json.dumps(self.data2) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"],"Input a password that is at least 8 characters long")

    def test_special_characters(self):
        """ Test to check if the username has any special characters  """
        response = self.app.post('/api/v1/auth/register', data = json.dumps(self.data3) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Username should not have special characters (. , ! space [])")

    def test_pass_special_characters(self):
        """ Test to check if the password has any special characters  """
        response = self.app.post('/api/v1/auth/register', data = json.dumps(self.data4) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Password should have atleast one number, small letter, capital letter and special character")

    def test_username_length(self):
        """ Test to check if the user username has the desired length """
        response = self.app.post('/api/v1/auth/register', data = json.dumps(self.data5) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"],"Username should be atleast 6 characters")

    def test_invalid_email(self):
        """ Test to check if the user entered an invalid email  """
        response = self.app.post('/api/v1/auth/register', data = json.dumps(self.data6) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Please a provide a valid email")
    
    def test_password_mismatch(self):
        """ Test to check if the users password are not matching"""
        response = self.app.post('/api/v1/auth/register', data = json.dumps(self.data7) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Password do not match")

    def test_valid_login(self):
        """ Test to check if the user log in successfully """
        response = self.app.post('/api/v1/auth/login', data = json.dumps(self.data1) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Successfully logged in to weConnect API. Create a Business page!")
   
    def test_login_password_mismatch(self):
        """ Test to check if the users login password is incorrect"""
        response = self.app.post('/api/v1/auth/login', data = json.dumps(self.data8) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Incorrect password")

    def test_registered_user(self):
        """ Checking if the user has an account """
        response = self.app.post('/api/v1/auth/login', data = json.dumps(self.data9) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "You have no account,please sign up")

    def test_change_password(self):
        """ Checking if the user changed password successfully """
        response = self.app.post('/api/v1/auth/login', data = json.dumps(self.data) , content_type = 'application/json')
        response1 = self.app.post('/api/v1/auth/reset-password', data = json.dumps(self.data10) , content_type = 'application/json')
        result = json.loads(response1.data.decode())
        self.assertEqual(result["message"], "Password changed successful")

    def test_new_password_match(self):
        """ Checking if the new password match """
        response = self.app.post('/api/v1/auth/login', data = json.dumps(self.data) , content_type = 'application/json')
        response1 = self.app.post('/api/v1/auth/reset-password', data = json.dumps(self.data11) , content_type = 'application/json')
        result = json.loads(response1.data.decode())
        self.assertEqual(result["message"], "The new passwords should match")


if __name__ == '__main__':
    unittest.main()

