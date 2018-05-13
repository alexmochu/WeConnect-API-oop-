import unittest

from flask import json
# local import
from api.views import app

class TestBusinessItemsTestCases(unittest.TestCase):
    """ Category Items tests case """

    def setUp(self):
        """ Setup category Class test case """
        app.testing = True
        self.app = app.test_client()
        self.data = {"email":"mochualex4@gmail.com", "username":"chairman", "password":"qweR12#$", "confirm_password":"qweR12#$"}
        self.data1 = {"category":"matajikko"}
        self.data2 = {"category":"matajikkowe"}
        self.data3 = {"category":"mata"}
        self.data4 = {"category":"matajikk&*(owe"}

        self.app.post('/api/v1/auth/register', data=json.dumps(self.data), content_type='application/json')
        self.app.post('/api/v1/auth/login', data=json.dumps(self.data), content_type='application/json')
        self.app.post('/api/v1/category', data=json.dumps(self.data1), content_type='application/json')
    
    def test_category_exists(self):
        """ Test to check if the category already exists """
        response = self.app.post('/api/v1/category', data = json.dumps(self.data1) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Please enter a Unique category name, category name already taken")
    
    def test_category_length(self):
        """ Test to check if the category name length is enough """
        response = self.app.post('/api/v1/category', data = json.dumps(self.data3) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Input a category name that is atleast 6 characters")
    
    def test_category_name_characters(self):
        """ Test to check if the category name has special characters """
        response = self.app.post('/api/v1/category', data = json.dumps(self.data4) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Category name should not contain special characters")
    
    def test_category_created(self):
        """ Test to check if the category added successfuly """
        response = self.app.post('/api/v1/category', data = json.dumps(self.data2) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Category added successfully. Add another category")

if __name__ == '__main__':
    unittest.main()