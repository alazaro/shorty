from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from utils.tests import fixtures

from ..models import ShortURL


class ShortURLTestCase(TestCase):
    def setUp(self):
        User.objects.create(**(fixtures.ONE_USER_PREPARED_DATA[0]))

    def test_unique_original(self):
        ShortURL.objects.create(original='http://google.com')
        self.assertRaises(
            ValidationError,
            ShortURL.objects.create,
            original='http://google.com')

    def test_reassign_short_if_exists(self):
        url1 = ShortURL.objects.create(original='http://google.com')
        url2 = ShortURL.objects.create(
            original='http://google.es', short=url1.short)
        self.assertNotEqual(url1.short, url2.short)

    def test_str(self):

        url = 'http://google.com'
        short = 'abcd'
        short_url = ShortURL(original=url, short=short)
        self.assertEqual(str(short_url), 'abcd -> http://google.com')
