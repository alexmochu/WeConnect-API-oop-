# api/__init__.py

# local import
from api.views import app

"""Initialize the app"""
def create_app():
    return app