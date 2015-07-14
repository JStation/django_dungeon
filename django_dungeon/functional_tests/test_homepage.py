from .base import FunctionalTest
from selenium import webdriver


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

class NewVisitorTest(FunctionalTest):

    def test_can_create_an_adventure_and_retrieve_it_later(self):
        # User opens browser and navigates to url
        self.browser.get(self.live_server_url)

        # User sees description of django dungeon below header
        # and learns that she can create and play text adventures
        description = self.browser.find_element_by_id("id_welcome_description")
        self.assertIn("Create, play and share text adventures.", description.text)

        # She is invited to create a new adventure
        new_adventure_header = self.browser.find_element_by_id("id_new_adventure_header")
        self.assertIn("Start creating your own adventure", new_adventure_header.text)

        # She clicks the button to create a new adventure
        with self.wait_for_page_load(self, timeout=10):
            self.browser.find_element_by_tag_name('button').click()

        # This redirects her to a 'new adventure' page
        self.assertEqual(self.browser.current_url, "test", "intentional fail, fix test")

        # She types "Haunted House Mystery" into the "title" box
        inputbox = self.browser.find_element_by_id('id_adventure_title')
        inputbox.send_keys('Haunted House Mystery')

        # She notices that the option 'Publish Adventure' is unchecked
        checkbox = self.browser.find_element_by_id('id_publish_checkbox')
        self.assertFalse(checkbox.is_selected(), "Publish checkbox is selected")

        # She checks the button
        checkbox.click()
        self.assertTrue(checkbox.is_selected(), "Publish checkbox failed to select")

        # She clicks the 'save' button to save the adventure
        self.browser.find_element_by_id('id_save_button').click()

        # And is redirected to the homepage containing a list of "latest stories",
        # with hers in the list
        self.wait_for_element_with_id('id_adventure_table') # Explicit wait
        table = self.browser.find_element_by_id('id_adventure_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('Haunted House Mystery', rows.text)

        # #####
        self.fail('Finish the Functional Test')




if __name__ == '__main__':
    unittest.main()
