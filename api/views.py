# api/__init__.py
from flask import jsonify, request, session
from flask_api import FlaskAPI

# local imports
from api.user_accounts import UserClass

# Initialize the api
app = FlaskAPI(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')


user_object = UserClass()

# Home route
@app.route('/')
def home_route():
    """ Home route """
    response = jsonify({'greetings': 'Greetings and welcome to weConnect API'})
    return response

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