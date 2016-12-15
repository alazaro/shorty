from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from ..models import ShortURL


class ShortURLCreateViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test_username')

    def test_from_creates_url(self):
        url = 'http://google.com'
        self.client.post(
            reverse('index'), data={'original': url})
        self.assertEqual(ShortURL.objects.first().original, url)

    def test_empty_url(self):
        response = self.client.post(
            reverse('index'), data={'original': ''})
        self.assertContains(response, 'This field is required')

    def test_form_returns_existing_url(self):
        url = 'http://google.com'
        self.client.post(
            reverse('index'), data={'original': url})
        short_url = ShortURL.objects.first()
        response = self.client.post(
            reverse('index'), data={'original': url})
        self.assertRedirects(response, short_url.get_absolute_url())

    def test_redirect_view(self):
        url = 'http://google.com'
        short_url = ShortURL.objects.create(original=url)
        response = self.client.get(
            reverse('redirect', args=[short_url.short])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, url)


class NoUsersTestCase(TestCase):
    def test_no_users(self):
        url = 'http://google.com'
        response = self.client.post(
            reverse('index'), data={'original': url})
        self.assertContains(
            response,
            'There are no users in the database.'
            ' Please run create_fake_users.')
