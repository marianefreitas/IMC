from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import home, login_user, logout_user, dashboard, turmas


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_user)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout_user)

    def test_dashboard_url_is_resolved(self):
        url = reverse('dashboard')
        self.assertEqual(resolve(url).func, dashboard)

    def test_turmas_url_is_resolved(self):
        url = reverse('turmas')
        self.assertEqual(resolve(url).func, turmas)
