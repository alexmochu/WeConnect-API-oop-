# api/business_reviews.py

#imports
import uuid

# local imports
from api.businesses import BusinessesClass

business_object = BusinessesClass

class ReviewsClass(object):
    """ Handles creation of reviews """

    def __init__(self):
        """ list to hold businesses reviews """
        self.reviews_list = []

    def add_review(self, business_id, user, review):
        """ handles creation of business reviews """
        # dictionary to hold reviews key and value
        review_dict = {}
        business_owner = [owner for owner in self.reviews_list if owner["owner"] == user and owner["business_id"] == business_id]
        if not business_owner:
            review_dict['review_id'] = str(uuid.uuid4())
            review_dict['business_id'] = business_id
            review_dict['owner'] = user
            review_dict['review'] = review
            self.reviews_list.append(review_dict)
            print(review_dict)
            print(self.reviews_list)
            response = {"message":"Successfully reviewed a business"}
            return response
        response = {"message":"You have already reveiwed this business"}
        return response

    def get_all_business_reviews_by_id(self):
        """ handles getting all reviews """
        if len(self.reviews_list) == 0:
            repsonse = {"message":"The business has no reviews yet. Be the first to review"}
            return repsonse
        return self.reviews_list
    