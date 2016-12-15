from copy import deepcopy
from unittest.mock import patch

from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.test import TestCase

from ..users import FakeUserGenerator, get_random_user
from .import fixtures


class FakeUserGeneratorTestCase(TestCase):
    @patch('utils.users.FakeUserGenerator.get_random_user_data')
    def test_create_one_user(self, random_data_mock):
        random_data_mock.return_value = fixtures.ONE_USER_PREPARED_DATA
        generator = FakeUserGenerator(1)
        generator.create_users()
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    @patch('utils.users.FakeUserGenerator.request_data')
    def test_get_random_user_data(self, request_data_mock):
        request_data_mock.return_value = fixtures.RANDOM_USER_JSON_RESPONSE
        generator = FakeUserGenerator(1)
        user_data = generator.get_random_user_data()
        expected_data = deepcopy(fixtures.ONE_USER_PREPARED_DATA)

        password = user_data[0].pop('password')
        expected_password = expected_data[0].pop('password')
        self.assertTrue(check_password(expected_password, password))

        self.assertEqual(
            user_data, expected_data
        )


class RandomUserTestCase(TestCase):
    def setUp(self):
        User.objects.create(**fixtures.ONE_USER_PREPARED_DATA[0])

    def test_get_random_user(self):
        random_user = get_random_user()
        self.assertIsInstance(random_user, User)
