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
        cpassword = request.json['cpassword']
        msg = user_object.register(username, email, password, cpassword)
        response = jsonify(msg)
        response.status_code = 201
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

# Create and view businesses
@app.route('/api/v1/business', methods=['GET', 'POST'])
def create_business():
    """ create event """
    if session.get('username') is not None:
        if request.method == "POST":
            business_name = request.json['business_name']
            user = request.json['user']
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

# Logout and remove session
@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    """ Logging out """
    if session.get('username') is not None:
        session.pop('username', None)
        return jsonify({"message": "Logout successful"})
    return jsonify({"message": "You are not logged in"})