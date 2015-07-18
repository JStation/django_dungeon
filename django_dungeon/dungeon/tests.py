from django.test import Client, TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
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

class NewAdventureFormTest(TestCase):

    def test_form_renders_title_input_has_placeholder_and_css_classes(self):
        form = NewAdventureForm()
        self.assertIn('placeholder="The Mysterious Quest"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_title(self):
        form = NewAdventureForm(data={'title': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['title'],
            ["Your adventure needs a title!"]
        )

    def test_form_has_submit_button_with_correct_css_and_attributes(self):
        # This test assumes the submit button is the first input added to FormHelper
        form = NewAdventureForm()
        print(form.helper.inputs[0].field_classes)
        print(form.helper.inputs[0].id)
        self.assertIn('btn-primary', form.helper.inputs[0].field_classes)
        self.assertIn('id_save_button', form.helper.inputs[0].id)

