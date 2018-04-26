# api/businesses
import re
import uuid

class BusinessesClass(object):
    """Handles creation of business items"""
    def __init__(self):
        """ list to hold events a user creates """
        self.businesses_list = []

    def getOwner(self, user):
        """ Returns businesses belonging to a user """
        user_business_list = [business for business in self.businesses_list if business['owner'] == user]
        return user_business_list

    def get_all_businesses(self):
        """Gets and Displays all Business items created and stored in the business lists"""
        if len(self.businesses_list) == 0:
            repsonse = {"message":"The Business catalog is empty. Create a business"}
            return repsonse
        return self.businesses_list

    def get_business(self, business_id):
        """Get a business by its ID"""
        #Check if business exists in business_list
        for business in self.businesses_list:
            if business_id == business['id']:
                return business
            else:
                response = {"message":"Business not found. Please search an already created business"}
        return response 

    def create_business(self, business_name, user, category, location):
        """Handles creation of events"""
        business_dict = {}
        #Check for special characters
        for business in self.businesses_list:
            if business_name == business["business_name"]:
                response = {"message":"Please enter a Unique business name, business name already taken"}
                return response

        if len(business_name) < 6:
            response = {"message":"Input a business name that is atleast 6 characters"}
            return response

        elif not re.match("^[a-zA-Z0-9 _]*$", business_name):
            response = {"message": "Business name should not contain special characters"}
            return response

        elif len(category) < 6:
            response = {"message":"Your category name should be atleast 6 characters"}
            return response

        elif len(location) < 5:
            response = {"message":"Your location name should be atleast 5 characters"}
            return response
        elif len(user) > 6:
            business_dict['id'] = str(uuid.uuid4())
            business_dict['business_name'] = business_name
            business_dict['owner'] = user
            business_dict['category'] = category
            business_dict['location'] = location
            self.businesses_list.append(business_dict)
        else:
            response = {"message":"User name length is less than 6 characters"}
            return response
        response = {"message":"Business added successfully. Add another business page"}
        return response

    def update_business(self, edit_business_name, old_business_name, user):
        """ handles updating of a business """
        if re.match("^[a-zA-Z0-9 _]*$", edit_business_name):
            #Get users lists
            my_businesses = self.getOwner(user)
            businesses = [business for business in my_businesses if business["business_name"] == old_business_name]
            if not businesses:
                return "Update Failed. You can only update business that you already created and own"
            found_business = businesses[0]
            del found_business['business_name']
            business_dict = {
                    'business_name': edit_business_name
                }
            found_business.update(business_dict)
            return self.getOwner(user)             
        else:
            return "No special characters (. , ! space [] )"

    def delete_business(self, business_id, user):
        """Handles removal of businesses"""
        #Checks if a business exists before deleting
        for business in self.businesses_list:
            if user == business["owner"]:
                if business_id == business["id"]:
                    self.businesses_list.remove(business)
                    response = {"message":"Business deleted successfully"}
                    return response
            else:
                response = {"message":"Unable to Delete. Please delete a business you own"}
                return response
        response = {"message":"The business you want to delete cannot be found or has not been created"}
        return response