# api/__init__.py
from flask import jsonify, request, session
from flask_api import FlaskAPI

# local imports
from api.user_accounts import UserClass
from api.businesses import BusinessesClass

# Initialize the api
app = FlaskAPI(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')


user_object = UserClass()
business_object = BusinessesClass()

# Home route
@app.route('/')
def home_route():
    """ Home route """
    response = jsonify({'greetings': 'Greetings and welcome to weConnect API'}), 200 #success
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
    return jsonify({"message": "Please Login"}), 401 #unauthorized

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
    return jsonify({"message": "Please login to get business"}), 401 #unauthorized

@app.errorhandler(403)
def forbidden():
    response = {"message":"You do not have enough permision to access this route"}
    return response, 403

@app.errorhandler(404)
def page_not_found():
    response = {"message":"Sorry. What you are looking for cannot be found."}
    return response, 404

@app.errorhandler(500)
def internal_server_error():
    response = {"message":"The server encountered an internal error. Thats all I know"}
    return response, 500

# Route for finding a business by its ID
@app.route('/api/v1/business/<business_id>', methods=['GET'])
def get_business(business_id):
    """Get Business by ID"""

    if session.get('username') is not None:
        if request.method == "GET":
            msg = business_object.get_business(business_id)
            response = jsonify(msg)
            return response
    return jsonify({"message": "Please login to get business"}), 401 #unauthorized

# Route for deleting business by its ID
@app.route('/api/v1/business/<business_id>', methods=['DELETE'])
def delete_business(business_id):
    """Delete Business by ID"""

    if session.get('username') is not None:
        business_name = business_id
        user = session["username"]
        delete_business_by_id = business_object.delete_business(business_name, user)
        return jsonify(delete_business_by_id)
    return jsonify({"message": "Please login to delete a business"}), 401 #unauthorized


# Logout and remove session
@app.route('/api/v1/auth/logout', methods=['GET', 'POST'])
def logout():
    """ Logging out """
    if session.get('username') is not None:
        session.pop('username', None)
        return jsonify({"message": "Logout successful"})
    return jsonify({"message": "You are not logged in"}), 401 #unauthorized