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
        self.assertIn("create and play text adventures", description.text)

        # She is invited to create a new adventure
        inputbox = self.browser.find_element_by_id('id_new_adventure')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Name of your new adventure'
        )

        # She types "Haunted House Mystery" into text box
        inputbox.send_keys('Haunted House Mystery')

        # When she hits enter she is redirected to a new page
        # that has the name of her adventure at the top
        # TODO: Explicit wait here?
        inputbox = self.browser.find_element_by_id('id_adventure_name')
        self.assertEqual(inputbox.text, 'Haunted House Mystery')

        # She notices that the option 'Publish Adventure' is unchecked
        checkbox = self.browser.find_element_by_id('id_publish_checkbox')
        self.assertFalse(checkbox.is_selected(), "Publish checkbox is selected")

        # She clicks the 'save' button to save the adventure
        self.browser.find_element_by_id('id_save_button').click()

        # And is redirected to a page containing a list of stories, with hers in the list
        # TODO: explicit wait here?
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('Haunted House Mystery', rows.text)

        # #####
        self.fail('Finish the Functional Test')




if __name__ == '__main__':
    unittest.main()
