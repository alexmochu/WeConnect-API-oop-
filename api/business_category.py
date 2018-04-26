# api/business_category.py

# import
import re
import uuid

class CategoryClass(object):
    """ Handels creation of Categories """
    def __init__(self):
        """ List hold categories """
        self.category_list = []

    def get_owner(self, user):
        """ handles category belonging to user """
        user_category_list = [category for category in self.category_list if category['owner'] == user]
        return user_category_list
    
    def get_all_categories(self):
        """ Gets all created categories """
        if len(self.category_list) == 0:
            response = {"message":"No categories created at the moment. Please create one for us"}
            return response
        return self.category_list

    def get_category(self, category_name):
        """ Find category by name """
        for category in self.category_list:
            if category_name == category['category']:
                return category
            else:
                response = {"message":"Category not found. Please search an already created category"}
        return response 

    def check_category(self, category_name):
        """ Checks if category is created """
        for category in self.category_list:
            if category_name == category['category']:
                return category_name
            else:
                response = {"message":"Category not found. Please create a new category or use one that is already created"}
        return response

    def create_category(self, category_name, user):
        """ Create a category """
        category_dict = {}
        for category in self.category_list:
            if category_name == category["category"]:
                response = {"message":"Please enter a Unique category name, category name already taken"}
                return response
             
        if len(category_name) < 6:
            response = {"message":"Input a category name that is atleast 6 characters"}
            return response

        elif not re.match("^[a-zA-Z0-9 _]*$", category_name):
            response = {"message":"Category name should not contain special characters"}
            return response
        else:
            category_dict['id'] = str(uuid.uuid4())
            category_dict['category'] = category_name
            category_dict['owner'] = user
            self.category_list.append(category_dict)
            response = {"message":"Category added successfully. Add another category"}
            return response
        return response

    def update_category(self, edit_category_name, old_category_name, user):
        """ handles updating a category """
        if re.match("^[a-zA-Z0-9 _]*$", edit_category_name):
            #Get users lists
            my_categories = self.get_owner(user)
            categories = [category for category in my_categories if category["category"] == old_category_name]
            if not categories:
                return "Update Failed. You can only update business that you already created and own"
            found_category = categories[0]
            del found_category['category']
            category_dict = {
                    'category': edit_category_name
                }
            found_category.update(category_dict)
            return self.get_owner(user)             
        else:
            return "No special characters (. , ! space [] )"

    def delete_category(self, category_name, user):
        """Handles removal of categories"""
        #Checks if a category exists before deleting
        for category in self.category_list:
            if user == category["owner"]:
                if category_name == category["category"]:
                    self.category_list.remove(category)
                    response = {"message":"Category deleted successfully"}
                    return response
            else:
                response = {"message":"Unable to Delete. Please delete a category you created"}
                return response
        response = {"message":"The category you want to delete cannot be found or has not been created"}
        return response