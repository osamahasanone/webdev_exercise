from faker import Faker
from models import db
from models.user import User

fake = Faker()


def create_dummy(n):
    '''create dummy users'''
    for i in range(n):
        user = User(name=fake.name())
        db.session.add(user)


def delete_all():
    '''delete all users and their skills relationships'''
    for user in User.query.all():
        user.skills = []
    User.query.delete()
