from flask import jsonify
from app.api import bp
from app.models import Users


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
    user = Users.query.first() or Users(username='world')
    return jsonify({'message': f'Hello, {user.username}!'})
