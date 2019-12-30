from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def resource_not_found(e):
    '''Handles 404 errors

    Args:
        e (werkzeug.exceptions.HTTPException): The exception thrown by an endpoint

    Returns:
        function: A jsonify()'d representation of the exception
        int: The HTTP status code
    '''
    return jsonify(error=str(e)), 404


def create_app(config=Config):
    '''Initializes the application

    Responsible for configuring and creating the Flask app, registering error
    handlers, initializing the database connection, and registering blueprints.

    Args:
        config (Config): An object containing configuration variables

    Returns:
        Flask: An instance of a configured Flask application
    '''
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_error_handler(404, resource_not_found)
    db.init_app(app)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app


from app import models
