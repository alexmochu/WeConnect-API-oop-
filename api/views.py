# api/__init__.py

from flask import jsonify
from flask_api import FlaskAPI

 # Initialize the api
app = FlaskAPI(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
 
# Home route
@app.route('/')
def home_route():
    response = jsonify({'greetings': 'Greetings and welcome to weConnect API'})
    return response