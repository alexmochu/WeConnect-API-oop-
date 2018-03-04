# config.py

class Config(object):
    """ Common or Parent configuration class."""

class DevelopmentConfig(Config):
    """ Development Configurations"""

    DEBUG = True
    SECRET_KEY = "scarface_tony_montana"

class TestingConfig(Config):
    """ Testing Configurations"""

    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    """ Configurations for Production."""

    DEBUG = True

app_config = {
    """ Environment Configuration Specification """

    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}