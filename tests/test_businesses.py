""" File to handle Unit Test for Business Items """
import unittest
# local imports
from api.businesses import BusinessesClass

class TestBusinessItemsTestCases(unittest.TestCase):
    """ Business Items tests case """

    def setUp(self):
        """ Setup Business Class Class test case """
        self.business_item_class = BusinessesClass()

    def test_special_characters_business_name(self):
        """ Check for special characters while creating a business item """
        user = "chairman"
        msg = self.business_item_class.create_business("Ma@en_deleo", user, "soft*%ware", "nairo@&")
        print(msg)
        self.assertEqual(msg, {"message":"Business name should not contain special characters"})

    def test_get_all_businesses(self):
        """ Check for all businesses """
        self.business_item_class.businesses_list = [{"owner": "chairman", "business_name":"Maendeleo", "category":"Backaend", "location":"myhomecity"}, {"owner": "chairmanwe", "business_name":"NshMaendeleo", "category":"Backaend", "location":"myhomecity"}]
        msg = self.business_item_class.businesses_list

        value = self.business_item_class.get_all_businesses()
        self.assertEqual(msg, value)

    def test_owner(self):
        """ Check for businesses belonging to owner """
        self.business_item_class.businesses_list = [{"owner": "chairman", "business_name":"Maendeleo", "category":"Backaend", "location":"myhomecity"},
                                                 {"owner": "chairmanwe", "business_name":"NshMaendeleo", "category":"Backaend", "location":"myhomecity"}]
        user = "chairman"
        msg = self.business_item_class.getOwner(user)
        self.assertEqual(msg, [{"owner": "chairman", "business_name":"Maendeleo", "category":"Backaend", "location":"myhomecity"}])

    def test_correct_output(self):
        """ Check for correct business creation """
        user = "chairman"
        msg = self.business_item_class.create_business("Maendeleo", user, "soft*%ware", "nairo@&")
        self.assertEqual(msg, {"message":"Business added successfully. Add another business page"})

    def test_update_business(self):
        """ Check for edits to business name """
        self.business_item_class.businesses_list = [{"owner": "chairman", "business_name":"Maendeleo", "category":"Backaend", "location":"myhomecity"},
                                                 {"owner": "chairmanwe", "business_name":"NshMaendeleo", "category":"Backaend", "location":"myhomecity"}]
        msg = self.business_item_class.update_business("Christmass", "Maendeleo", "chairman")
        self.assertEqual(msg, [{"owner": "chairman", "business_name":"Christmass", "category":"Backaend", "location":"myhomecity"}])
    
    def test_unique_business_name(self):
        """ check for unique business name """
        self.business_item_class.businesses_list = [{"owner": "chairman", "business_name":"Maendeleo", "category":"Backaend", "location":"myhomecity"},
                                                 {"owner": "chairmanwe", "business_name":"NshMaendeleo", "category":"Backaend", "location":"myhomecity"}]
        user = "chairman"
        msg = self.business_item_class.create_business("Maendeleo", user, "soft*%ware", "nairo@&")
        self.assertEqual(msg, {"message":"Please enter a Unique business name, business name already taken"})

    def test_min_business_name_length(self):
        """ check minimum business length """
        self.business_item_class.businesses_list = [{"owner": "chairman", "business_name":"Maendeleo", "category":"Backaend", "location":"myhomecity"},
                                                 {"owner": "chairmanwe", "business_name":"NshMaendeleo", "category":"Backaend", "location":"myhomecity"}]
        user = "chairman"
        msg = self.business_item_class.create_business("Mdleo", user, "soft*%ware", "nairo@&")
        self.assertEqual(msg, {"message":"Input a business name that is atleast 6 characters"}) 

    def test_min_category_name_length(self):
        """ check minimum category length """
        self.business_item_class.businesses_list = [{"owner": "chairman", "business_name":"Maendeleo", "category":"Backaend", "location":"myhomecity"},
                                                 {"owner": "chairmanwe", "business_name":"NshMaendeleo", "category":"Backaend", "location":"myhomecity"}]
        user = "chairman"
        msg = self.business_item_class.create_business("Mafeendeleo", user, "sore", "nairo@&")
        self.assertEqual(msg, {"message":"Your category name should be atleast 6 characters"})    

    def test_min_location_name_length(self):
        """ check minimum location length """
        self.business_item_class.businesses_list = [{"owner": "chairman", "business_name":"Maendeleo", "category":"Backaend", "location":"myhomecity"},
                                                 {"owner": "chairmanwe", "business_name":"NshMaendeleo", "category":"Backaend", "location":"myhomecity"}]
        user = "chairman"
        msg = self.business_item_class.create_business("Mafeendeleo", user, "software", "nai")
        self.assertEqual(msg, {"message":"Your location name should be atleast 5 characters"})    

    def test_min_user_name_length(self):
        """ check minimum username length """
        self.business_item_class.businesses_list = [{"owner": "chairman", "business_name":"Maendeleo", "category":"Backaend", "location":"myhomecity"},
                                                 {"owner": "chairmanwe", "business_name":"NshMaendeleo", "category":"Backaend", "location":"myhomecity"}]
        user = "chan"
        msg = self.business_item_class.create_business("Mafeendeleo", user, "software", "nairobi")
        self.assertEqual(msg, {"message":"User name length is less than 6 characters"})    

    def tearDown(self):
        """ Teardown Business Class test case  """
        del self.business_item_class

if __name__ == '__main__':
    unittest.main()