import click
from sqlalchemy.exc import SQLAlchemyError
from app import db
from app.models import User


def register(app):
    @app.cli.group()
    def init():
        '''Initiliazes various parts of the application'''
        pass

    @init.command()
    def tables():
        '''Creates empty database tables based on models'''
        print('Initializing database tables...')
        result = db.create_all()
        db.session.commit()

    @init.command()
    def user():
        '''Creates a test user'''
        print('Creating test user...')
        u = User(username='test', email='test@test.com')

        try:
            db.session.add(u)
            db.session.commit()
            print(f'Successfully added {u}')
        except SQLAlchemyError as e:
            print(f'Failed to add {u}')
            print(e)
