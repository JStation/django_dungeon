from django.test import TestCase

from dungeon.models import Adventure


class HomePageViewTest(TestCase):

    def test_view_returns_list_of_adventures(self):
        a_title = "Test Adventure"
        adventure_ = Adventure.objects.create(title=a_title)
        response = self.client.get('/')
        self.assertContains(response, a_title)

