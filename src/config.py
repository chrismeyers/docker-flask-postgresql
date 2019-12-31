import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    '''Defines global application configuration

    Attributes:
        SQLALCHEMY_DATABASE_URI (str): Database connection URI
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Enables or disables the
            Flask-SQLAlchemy event system
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    '''Defines global application configuration for tests

    Attributes:
        TESTING (bool): Controls error catching during request handling. Setting
            to True provides better error reports when performing test requests
            against the application.
        SQLALCHEMY_DATABASE_URI (str): Database connection URI
    '''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')
