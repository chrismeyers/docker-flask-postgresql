from flask import jsonify
from app.api import bp
from app.models import User


@bp.route('/')
def greet():
    ''' Hello World endpoint
    ---
    get:
        summary: Greets a user, or the World
        description: Example endpoint
        responses:
            200:
                description: A greeting to someone
    '''
    user = User.query.first() or User(username='world')
    return jsonify({'message': f'Hello, {user.username}!'})
