import random
import string

from dateutil.parser import parse

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

import requests


class FakeUserGenerator:
    def __init__(self, user_count):
        self.user_count = user_count

    def request_data(self):
        return requests.get(
            'https://randomuser.me/api/?results={0}'.format(
                self.user_count)).json()

    def get_random_user_data(self):
        """Adapt the data that came from the API to be ready to create `User`
        objects
        """
        json = self.request_data()['results']
        return [{
            'username': u['login']['username'],
            'password': make_password(u['login']['password']),
            'email': u['email'],
            'first_name': u['name']['first'],
            'last_name': u['name']['last'],
            'date_joined': parse(u['registered'] + 'UTC'),
        } for u in json]

    def create_users(self):
        users_data = self.get_random_user_data()
        User.objects.bulk_create((
            User(**user_data) for user_data in users_data
        ))


class NoUsersException(Exception):
    pass


def get_random_user():
    count = User.objects.count()
    if count:
        random_position = random.randint(0, count - 1)
        return User.objects.all()[random_position:random_position + 1][0]
    else:
        raise NoUsersException(
            'There are no users in the database.'
            ' Please run create_fake_users.')


def get_random_string():
    characters = string.ascii_letters + string.digits
    return ''.join(random.sample(characters, settings.SHORT_URL_MAX_LEN))
