from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home(self):
        response = self.client.get(reverse('home'))

        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_login(self):
        response = self.client.get(reverse('login'))

        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_logout(self):
        response = self.client.get(reverse('logout'))

        self.assertAlmostEqual(response.status_code, 302)
