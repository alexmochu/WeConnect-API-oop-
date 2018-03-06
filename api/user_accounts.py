# api/useraccounts.py

""" Provides regular expression matching operations """
import re

""" User class handles registration and login of users """
class UserClass(object): 
    def __init__(self):
        self.users_list = []
    
    def register(self, username, email, password, cpassword):
        """ Create user accounts by user info to empty dictonary """
        user_dict = {}

        for user in self.users_list:
            if username == user['username']:
                return "Account already exists. Please login or Recover account"
            elif email == user['email']:
                return "Account already exists. Please login or Recover account"

        if len(password) < 8:
            return "Input a password that is at least 8 characters long"

        elif not re.match("^[a-zA-Z0-9_]*$", username):
            return "Username should not have special characters (. , ! space [])"

        elif not re.match(r"(^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-z]+$)", email):
            return "Please a provide a valid email"

        elif password == cpassword:
            user_dict['username'] = username
            user_dict['email'] = email
            user_dict['password'] = password

            self.users_list.append(user_dict)
        else:
            return "Password do not match"
        
        return "Successfully created a weConnect Business Account. You can login!"
        
