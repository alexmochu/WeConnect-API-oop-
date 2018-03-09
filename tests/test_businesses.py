""" File to handle Unit Test for Business Items """
import unittest
from api.businesses import BusinessesClass

class TestBusinessItemsTestCases(unittest.TestCase):
    """ Business Items tests case """

    def setUp(self):
        """ Setup Business Class Class test case """

        self.business_item_class = BusinessesClass()


    def tearDown(self):
        """ Teardown Business Class test case  """

        del self.business_item_class

if __name__ == '__main__':
    unittest.main()