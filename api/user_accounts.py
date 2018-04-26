# api/useraccounts.py

""" Provides regular expression matching operations """
import re
class UserClass(object):
    """ User class handles registration and login of users """
    def __init__(self):
        # list to hold user details
        self.users_list = []

    def register(self, username, email, password, confirm_password):
        """ Create user accounts by user info to empty dictonary """
        user_dictionary = {}

        for user in self.users_list:
            if username == user['username']:
                response = {"message":"Account already exists. Please login or Recover account"}
                return response
            elif email == user['email']:
                response = {"message":"Account already exists. Please login or Recover account"}
                return response
        if len(password) < 8:
            response = {"message":"Input a password that is at least 8 characters long"}
            return response

        elif not re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$", password):
            response = {"message":"Password should have atleast one number, small letter, capital letter and special character"}
            return response

        elif len(username) < 6:
            response = {"message":"Username should be atleast 6 characters"}
            return response

        elif not re.match("^[a-zA-Z0-9_]*$", username):
            response = {"message":"Username should not have special characters (. , ! space [])"}
            return response

        elif not re.match(r"(^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-z]+$)", email):
            response = {"message":"Please a provide a valid email"}
            return response

        elif password == confirm_password:
            user_dictionary['username'] = username
            user_dictionary['email'] = email
            user_dictionary['password'] = password
            self.users_list.append(user_dictionary)
        else:
            response = {"message":"Password do not match"}
            return response
        response = {"message":"Successfully created a weConnect Business Account. You can login!"}
        return response

    def login(self, username, password):
        """ Login user by checking if user exists in
            users_lisr
        """
        for user in self.users_list:
            if username == user['username']:
                if password == user['password']:
                    response = {"message":"Successfully logged in to weConnect API. Create a Business page!"}
                    return response
                response = {"message":"Incorrect password"}
                return response
        response = {"message":"You have no account,please sign up"}
        return response

    def change_password(self, new_password, confirm_password):
        """ Reset password """
        for user in self.users_list:
            if new_password == confirm_password:
                user['password'] = new_password
                response = {"message":"Password changed successful"}
                return response
            response = {"message":"The new passwords should match"}
            return response
        response = {"message":"User does not exist, sign up!"} 
        return response