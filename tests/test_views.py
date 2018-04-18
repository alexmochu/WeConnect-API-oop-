
import api
import unittest
import json



class ApiTestCase(unittest.TestCase):

    def setUp(self):
        api.app.testing = True
        self.app = api.app.test_client()
        self.data = {"username":"chairman", "email":"email@gmail.com","password":"12345678", "confirm_password":"12345678"}
        self.data1 = {"username":"chairmanw2", "email":"emaiakll@gmail.com","password":"12345678", "confirm_password":"12345678"}
        self.data2 = {"username":"chassmanw2", "email":"emaiafgkll@gmail.com","password":"12345678", "confirm_password":"12345678"}
        self.data3 = {"id":"4683828373832829", "business_name":"Maendeleo", "category":"Backaend", "location":"myhomecity"}
        self.data4 = {"new_password": "tn&T4tyY", "confirm_password": "tn&T4tyY"}
    def test_register_user(self):
        response = self.app.post('/api/v1/auth/register', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Successfully created a weConnect Business Account. You can login!")
        self.assertEqual(response.status_code, 201)

    def test_duplicate_register(self):
        response1 = self.app.post('/api/v1/auth/register', data = json.dumps(self.data2) , content_type = 'application/json')
        result1 = json.loads(response1.data.decode())
        self.assertEqual(result1["message"], "Successfully created a weConnect Business Account. You can login!")
        self.assertEqual(response1.status_code, 201)
        response2 = self.app.post('/api/v1/auth/register', data = json.dumps(self.data2) , content_type = 'application/json')
        result2 = json.loads(response2.data.decode())
        self.assertEqual(result2["message"], "Account already exists. Please login or Recover account")
 
    def test_homepage(self):
        response = self.app.get('/', content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['greetings'], 'Greetings and welcome to weConnect API')

    def test_login(self):
        self.app.post('/api/v1/auth/register', data = json.dumps(self.data1) , content_type = 'application/json')
        response = self.app.post('/api/v1/auth/login', data = json.dumps(self.data1) , content_type = 'application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Successfully logged in to weConnect API. Create a Business page!")
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.app.post('/api/v1/auth/login', data = json.dumps(self.data1) , content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        response1 = self.app.post('/api/v1/auth/logout', data = json.dumps(self.data1) , content_type = 'application/json')
        result1 = json.loads(response1.data.decode())
        self.assertEqual(result1["message"], "Logout successful")
        self.assertEqual(response1.status_code, 200)

    
    def test_create_business(self):
        response = self.app.post('/api/v1/auth/login', data = json.dumps(self.data1) , content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        response1 = self.app.post('/api/v1/business', data = json.dumps(self.data3), content_type = 'application/json')
        result = json.loads(response1.data.decode())
        self.assertEqual(result["message"], "Business added successfully. Add another business page")
        self.assertEqual(response.status_code, 200)

    def test_reset_passoword(self):
        response = self.app.post('/api/v1/auth/login', data = json.dumps(self.data1) , content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        response2 = self.app.post('/api/v1/auth/reset-password', data = json.dumps(self.data4), content_type = 'application/json')
        result = json.loads(response2.data.decode())
        self.assertEqual(result["message"], "Password changed successful")
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.app.post('/api/v1/auth/login', data = json.dumps(self.data1) , content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        response2 = self.app.post('/api/v1/auth/logout', content_type = 'application/json')
        result = json.loads(response2.data.decode())
        self.assertEqual(result["message"], "Logout successful")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()