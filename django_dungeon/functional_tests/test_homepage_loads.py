from django.test import TestCase
from selenium import webdriver


class HomepageTest(TestCase):

    def test_homepage_content(self):
        # User opens browser and navigates to url
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000')

        # User notices site title in title bar
        self.assertIn('Django Dungeon', self.browser.title)

        # and welcome message on page
        welcomeBox = self.browser.find_element_by_id('id_welcome_banner')
        self.assertEqual(welcomeBox.text, 'Django Dungeon')

        # User closes browser
        self.browser.quit()

    def test_homepage_style(self):
        # User opens browser and navigates to url
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000')
        self.browser.set_window_size(1024, 768)

        # User notices that welcome banner is centered
        welcomeBox = self.browser.find_element_by_id('id_welcome_banner')
        self.assertAlmostEqual(
            welcomeBox.location['x'] + welcomeBox.size['width']/2,
            512,
            delta=10
        )

        # User closes browser
        self.browser.quit()




if __name__ == '__main__':
    unittest.main()
