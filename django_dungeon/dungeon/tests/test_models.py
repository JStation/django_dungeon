from django.test import TestCase

from dungeon.forms import NewAdventureForm
from dungeon.models import Adventure


class AdventureModelTest(TestCase):

    def test_default_title(self):
        adventure = Adventure()
        self.assertEqual(adventure.title, '')

    def test_get_absolute_url(self):
        form = NewAdventureForm(data={'title': 'A new adventure'})
        new_adventure = form.save()
        self.assertEqual('/edit/1/', new_adventure.get_absolute_url())
