from django.test import Client, TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from dungeon.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_template(self):
        c = Client()
        response = c.get('/')
        self.assertTemplateUsed(response, 'home.html')