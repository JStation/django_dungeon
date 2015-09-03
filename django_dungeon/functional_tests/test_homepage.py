from .base import FunctionalTest


class HomepageTest(FunctionalTest):

    def test_homepage_content(self):
        # User opens browser and navigates to url
        self.browser.get(self.live_server_url)

        # User notices site title in title bar
        self.assertIn('Django Dungeon', self.browser.title)

        # and welcome message on page
        welcomeBox = self.browser.find_element_by_id('id_welcome_header')
        self.assertEqual(welcomeBox.text, 'Django Dungeon')


    def test_homepage_style(self):
        # User opens browser and navigates to url
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # User notices that welcome banner is centered
        welcomeBox = self.browser.find_element_by_id('id_welcome_header')
        self.assertAlmostEqual(
            welcomeBox.location['x'] + welcomeBox.size['width']/2,
            512,
            delta=10
        )

        # User closes browser
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
