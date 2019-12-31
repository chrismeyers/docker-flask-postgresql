import pytest
from app.models import Users


@pytest.fixture()
def users(database):
    user1 = Users(username='test1', email='test1@test.com')
    user2 = Users(username='test2', email='test2@test.com')

    database.session.add_all([user1, user2])
    database.session.commit()


def test_users_exist(database, users):
    assert Users.query.count() == 2
    assert Users.query.filter(Users.username == 'test1').first().id == 1
    assert Users.query.filter(Users.username == 'test2').first().id == 2
