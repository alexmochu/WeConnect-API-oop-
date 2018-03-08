# api/businesses

class BusinessesClass(object):
    """Handles creation of events"""

    def __init__(self):
        """ list to hold events a user creates """
        self.businesses_list = []

    def get_all_businesses(self):
        """Gets and Displays all Business items created and stored in the business lists"""
        return self.businesses_list

    def get_business(self, business_id):
        """Get a business by its ID"""

        #Check if business exists in business_list
        for business in self.businesses_list:
            if business_id == business["business_name"]:
                return business

        return "Business not found. Please search an already created business"

    def create_business(self, business_name, user, category, location):
        """Handles creation of events"""
        business_dict = {}

        #Check for special characters
        for business in self.businesses_list:
            if business_name == business["business_name"]:
                return "Please enter a Unique business name, business name already taken"

        if len(business_name) < 6:
            return "Input a business name that is atleast 6 characters"

        elif len(category) < 6:
            return "Your caegory name should be atleast 6 characters"

        elif len(location) < 5:
            return "Your location name should be atleast 5 characters"

        elif len(user) > 6:
            business_dict['business_name'] = business_name
            business_dict['owner'] = user
            business_dict['category'] = category
            business_dict['location'] = location

            self.businesses_list.append(business_dict)
        else:
            return "User name length is less than 8 characters"
        return "Business added successfully. Add another business page"
