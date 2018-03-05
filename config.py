# config.py

class Config(object):
    """ Common or Parent configuration class."""
    DEBUG = True

class DevelopmentConfig(Config):
    """ Development Configurations"""

    DEBUG = True


class TestingConfig(Config):
    """ Testing Configurations"""

    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    """ Configurations for Production."""

    DEBUG = True