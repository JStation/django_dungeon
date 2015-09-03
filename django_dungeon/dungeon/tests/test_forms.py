from django.test import TestCase

from dungeon.forms import NewAdventureForm
from dungeon.models import Adventure


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
        self.assertIn('btn-primary', form.helper.inputs[0].field_classes)
        self.assertIn('id_save_button', form.helper.inputs[0].id)

    def test_form_save(self):
        form = NewAdventureForm(data={'title': 'Test Adventure'})
        new_adventure = form.save()
        print(Adventure.objects.all())
        self.assertEqual(new_adventure, Adventure.objects.all()[0])
