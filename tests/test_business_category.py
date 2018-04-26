import unittest
# local imports

from api.business_category import CategoryClass

class TestBusinessItemsTestCases(unittest.TestCase):
    """ Category Items tests case """

    def setUp(self):
        """ Setup category Class test case """
        self.category_item_class = CategoryClass()

    def test_owner(self):
        """ Check for businesses belonging to owner """
        self.category_item_class.category_list = [{"id":"234567123", "owner":"chairman", "category":"gfgfgfhsh"}]
        user = "chairman"
        msg = self.category_item_class.get_owner(user)
        self.assertEqual(msg, [{"id":"234567123", "owner":"chairman", "category":"gfgfgfhsh"}])

    def test_get_all_businesses(self):
        """ Check for all businesses """
        self.category_item_class.category_list = [{"owner": "chairman", "business_name":"Maendeleo", "category":"Backaend", "location":"myhomecity"}, {"owner": "chairmanwe", "business_name":"NshMaendeleo", "category":"Backaend", "location":"myhomecity"}]
        msg = self.category_item_class.category_list

        value = self.category_item_class.get_all_categories()
        self.assertEqual(msg, value)

    def tearDown(self):
        """ Teardown category Class test case  """
        del self.category_item_class

if __name__ == '__main__':
    unittest.main()