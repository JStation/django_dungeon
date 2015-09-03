from django.test import Client, TestCase
from django.core.urlresolvers import resolve

from dungeon.views import home_page, new_adventure
from dungeon.forms import NewAdventureForm


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_template(self):
        c = Client()
        response = c.get('/')
        self.assertTemplateUsed(response, 'home.html')

class NewAdventurePageTest(TestCase):

    def test_url_resolves_to_new_adventure_view(self):
        found = resolve('/new_adventure/')
        self.assertEqual(found.func, new_adventure)

    def test_new_adventure_page_returns_correct_template(self):
        c = Client()
        response = c.get('/new_adventure/')
        self.assertTemplateUsed(response, 'new_adventure.html')

    def test_new_adventure_page_uses_new_adventure_form(self):
        response = self.client.get('/new_adventure/')
        self.assertIsInstance(response.context['form'], NewAdventureForm)

    def test_form_redirects_after_posting_data(self):
        c = Client()
        response = c.post('/new_adventure/', {'title': 'Testing Adventure'})
        self.assertRedirects(response, '/edit/1/')
