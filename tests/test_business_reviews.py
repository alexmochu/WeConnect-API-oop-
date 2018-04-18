import unittest
from api.business_reviews import ReviewsClass

class TestBusinessItemsTestCases(unittest.TestCase):
    """ Review Items tests case """

    def setUp(self):
        """ Setup Review Class test case """

        self.review_item_class = ReviewsClass()

    def test_reviewed_business(self):
        """ Checking if business has already been reviewed """
        self.review_item_class.reviews_list = [{"review_id":"234567123", "business_id":"4512588399294", \
             "owner":"chairman", "review":"This is a review"}]
        msg = self.review_item_class.add_review("4512588399294", "chairman", "This is a review")
        self.assertEqual(msg, {"message":"You have already reveiwed this business"})

    def test_successfull_review(self):
        """ Check if business was succesfully reviewed"""
        msg = self.review_item_class.add_review("4512588399294", "chairman", "This is a review")
        self.assertEqual({"message":"Successfully reviewed a business"}, msg)


    def tearDown(self):
        """ Teardown Review Class test case  """

        del self.review_item_class
if __name__ == '__main__':
    unittest.main()