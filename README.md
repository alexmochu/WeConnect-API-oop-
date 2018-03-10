[![Build Status](https://travis-ci.org/alexmochu/WeConnect-API-oop-.svg?branch=api)](https://travis-ci.org/alexmochu/WeConnect-API-oop-) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/367332d3d766461f9109733d7dd486ce)](https://www.codacy.com/app/alexmochu/WeConnect-API-oop-?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=alexmochu/WeConnect-API-oop-&amp;utm_campaign=Badge_Grade) [![Coverage Status](https://coveralls.io/repos/github/alexmochu/WeConnect-API-oop-/badge.svg?branch=master)](https://coveralls.io/github/alexmochu/WeConnect-API-oop-?branch=master)

# WeConnect-API-oop-
WeConnect provides a platform that brings businesses and individuals together. This platform creates awareness for businesses and gives the users the ability to write reviews about the businesses they have interacted with.  

# Technology Used
The API has been built with:
- Flask micro-framework (Python 3.6)

# UI templates
- To preview the UI, proceed to https://alexmochu.github.io .
- The <a href="https://github.com/alexmochu/alexmochu.github.io">UI Templates</a> have been hosted on Github Pages

# Features
1.  Users can be able to register and create an account
2.  Registered users can be able to log in
3.  Once logged in, the user can create a business
4.  Each business created can has an ID and a unique business name
5.  Logged in users can query all businesses or a single business by its ID
6.  Only logged in users have the privilege of creating and viewing businesses

# Installation
1. Ensure you have installed Python3.6+, created and an activated a virtual environment.
2. Clone the repo in your local machine inside the virtual environment you have created.
3. Navigate to the project folder(WeConnect-API-oop-)
4. Install all the requirements of the project by typing: 
`pip install -r requirements.txt`

# Running the API
- Type:
`export FLASK_APP=run.py`
`flask run`

# Running the Tests
- Install Pytest : 
`pip install pytest`
- Run tests: 
`py.test`

# API Endpoints

| Resource URL | Methods | Description
|-------------- |------- |---------------
| /api/v1/auth/register | POST | User Registration
| /api/v1/auth/login    | POST | User Login
| /api/v1/auth/reset-password | POST | User can be able to reset password
| /api/v1/auth/logout | POST | Logs out User
| /api/v1/business | POST | Create a business with unique ID and business name
| /api/v1/business | GET | Retrive all business created
| /api/v1/business/<business_id> | GET | Retrive a business by ID


# UI Templates
![weconnecthomapage](https://user-images.githubusercontent.com/18735075/37186957-059ebe8c-2359-11e8-8c3a-2ae5d56c1267.png)
![signup](https://user-images.githubusercontent.com/18735075/37186858-a0eac12a-2358-11e8-825e-de23e9ea3212.png)![search](https://user-images.githubusercontent.com/18735075/37186864-ab162748-2358-11e8-98fc-8449e5837eaa.png)![login](https://user-images.githubusercontent.com/18735075/37186854-9b372502-2358-11e8-9271-eff2dee807b7.png)


