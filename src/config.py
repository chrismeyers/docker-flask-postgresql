import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    '''Defines global application configuration

    Attributes:
        SQLALCHEMY_DATABASE_URI (str): PostgreSQL database connection URL
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Enables or disables the
            Flask-SQLAlchemy event system
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
