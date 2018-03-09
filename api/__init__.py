# api/__init__.py

# local import
from api.views import app

def create_app():
    """Initialize the app"""
    return app