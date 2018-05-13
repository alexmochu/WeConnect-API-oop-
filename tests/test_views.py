# tests/test_views
import api
import unittest
import json
class ApiTestCase(unittest.TestCase):
    """ views tests case """

    def setUp(self):
        """ Setup api views test case """
        api.app.testing = True
        self.app = api.app.test_client()
        self.data = {"username":"chairman", "email":"email@gmail.com","password":"qwerW234#", "confirm_password":"qwerW234#"}
        self.data1 = {"username":"chairmanw2", "email":"emaiakll@gmail.com","password":"qwerW234#", "confirm_password":"qwerW234#"}
        self.data2 = {"username":"chassmanw2", "email":"emaiafgkll@gmail.com","password":"qwerW234#", "confirm_password":"qwerW234#"}
        self.data3 = {"id":"4683828373832829", "business_name":"Maendeleo", "category":"Backaend", "location":"myhomecity"}
        self.data4 = {"new_password": "tn&T4tyY", "confirm_password": "tn&T4tyY"}
        self.data5 = {"category": "Backaend"}


    def test_homepage(self):
        """ check homepage view"""
        response = self.app.get('/', content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['greetings'], 'Greetings and welcome to weConnect API')

    def test_logout(self):
        """ check logout view """
        response = self.app.post('/api/v1/auth/login', data = json.dumps(self.data1) , content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        response1 = self.app.post('/api/v1/auth/logout', data = json.dumps(self.data1) , content_type = 'application/json')
        result1 = json.loads(response1.data.decode())
        self.assertEqual(result1["message"], "Logout successful")
        self.assertEqual(response1.status_code, 200)

    def test_create_business(self):
        """check create business view  """
        response = self.app.post('/api/v1/auth/login', data = json.dumps(self.data1) , content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        self.app.post('/api/v1/category', data = json.dumps(self.data5) , content_type = 'application/json')
        response1 = self.app.post('/api/v1/business', data = json.dumps(self.data3), content_type = 'application/json')
        result = json.loads(response1.data.decode())
        self.assertEqual(result["message"], "Business added successfully. Add another business page")
        self.assertEqual(response.status_code, 200)

    def test_reset_passoword(self):
        """ check reset password view """
        response = self.app.post('/api/v1/auth/login', data = json.dumps(self.data1) , content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        response2 = self.app.post('/api/v1/auth/reset-password', data = json.dumps(self.data4), content_type = 'application/json')
        result = json.loads(response2.data.decode())
        self.assertEqual(result["message"], "Password changed successful")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()