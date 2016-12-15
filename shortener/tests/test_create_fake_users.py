from unittest.mock import patch
from unittest import TestCase  # We don't test DB

from django.core.management import call_command, CommandError


class CreateFakeUsersTestCase(TestCase):
    def test_command_fails_without_args(self):
        self.assertRaises(CommandError, call_command, 'create_fake_users')

    def test_command_fails_with_two_args(self):
        self.assertRaises(
            CommandError, call_command, 'create_fake_users', 1, 2)

    @patch('utils.users.FakeUserGenerator.create_users')
    def test_command_creates_one_user(self, create_users_mock):
        call_command('create_fake_users', 1)
        create_users_mock.assert_called_once_with()
