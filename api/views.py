# api/__init__.py
from flask import jsonify, request, session
from flask_api import FlaskAPI

# local imports
from api.user_accounts import UserClass
from api.businesses import BusinessesClass
from api.buiness_reviews import ReviewsClass

# Initialize the api
app = FlaskAPI(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')


user_object = UserClass()
business_object = BusinessesClass()
review_object = ReviewsClass()

# Home route
@app.route('/')
def home_route():
    """ Home route """
    response = jsonify({'greetings': 'Greetings and welcome to weConnect API'})
    return response

# Registration Route
@app.route('/api/v1/auth/register', methods=['GET', 'POST'])
def signup():
    """ User register """
    if request.method == "POST":
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        confirm_password = request.json['confirm_password']
        msg = user_object.register(username, email, password, confirm_password)
        response = jsonify(msg)
        response.status_code = 200
        return response

# Login Route
@app.route('/api/v1/auth/login', methods=['GET', 'POST'])
def login():
    """ User login """
    if request.method == "POST":
        username = request.json['username']
        password = request.json['password']
        session['username'] = username
        msg = user_object.login(username, password)
        response = jsonify(msg)
        response.status_code = 200
        return response

# Route for creating a business
@app.route('/api/v1/business', methods=['GET', 'POST'])
def create_business():
    """ create event """
    if session.get('username') is not None:
        if request.method == "POST":
            business_name = request.json['business_name']
            user = session["username"]
            location = request.json['location']
            category = request.json['category']

            msg = business_object.create_business(business_name, user, category, location)
            response = jsonify(msg)
            response.status_code = 201
            return response
        elif request.method == "GET":
            msg = business_object.get_all_businesses()
            response = jsonify(msg)
            return response
    return jsonify({"message": "Please Login"})

@app.route('/api/v1/business/<business_id>', methods=['PUT'])
def update_business(business_id):

    if session.get('username') is not None:
        if request.method == "PUT":
            user = session["username"]
            business = business_object.get_business(business_id)
            old_business_name = business['business_name']
            edit_business_name = request.json['edit_business_name']
            update_business_by_id = business_object.update_business(edit_business_name, old_business_name, user)
            return jsonify(update_business_by_id)
    return jsonify({"message": "Please Login update a business"})

# Route for reseting a users password
@app.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    """ Reseting password """
    if session.get('username') is not None:
        if request.method == "POST":
            new_password = request.json['new_password']
            confirm_password = request.json['confirm_password']
            msg = user_object.change_password(new_password, confirm_password)
            return msg
    return jsonify({"message": "Please login to get business"})

# Route for finding a business by its ID
@app.route('/api/v1/business/<business_id>', methods=['GET'])
def get_business(business_id):
    """Get Business by ID"""

    if session.get('username') is not None:
        if request.method == "GET":
            msg = business_object.get_business(business_id)
            response = jsonify(msg)
            return response
    return jsonify({"message": "Please login to get business"})

# Route for deleting business by its ID
@app.route('/api/v1/business/<business_id>', methods=['DELETE'])
def delete_business(business_id):
    """Delete Business by ID"""

    if session.get('username') is not None:
        if request.method == "DELETE":
            user = session["username"]
            delete_business_by_id = business_object.delete_business(business_id, user)
            return jsonify(delete_business_by_id)
    return jsonify({"message": "Please login to delete a business"})

@app.route('/api/v1/business/<business_id>/reviews', methods=['GET', 'POST'])
def add_review(business_id):

    if session.get('username') is not None:
        if request.method == "POST":
            business = business_object.get_business(business_id)
            business_unique_id = business["id"]
            user = session["username"]
            review = request.json['review']

            msg = review_object.add_review(business_unique_id, user, review)
            response = jsonify(msg)
            response.status_code = 201
            return response
        elif request.method == "GET":
            msg = review_object.get_all_business_reviews_by_id()
            response = jsonify(msg)
            return response
    return jsonify({"message": "Please Login to add Review"})


# Logout and remove session
@app.route('/api/v1/auth/logout', methods=['GET', 'POST'])
def logout():
    """ Logging out """
    if session.get('username') is not None:
        session.pop('username', None)
        return jsonify({"message": "Logout successful"})
    return jsonify({"message": "You are not logged in"})