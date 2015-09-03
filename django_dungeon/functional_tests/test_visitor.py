from .base import FunctionalTest


class VisitorTest(FunctionalTest):

    def test_can_create_an_adventure_and_retrieve_it_later(self):
        # User opens browser and navigates to url
        self.browser.get(self.live_server_url)

        # User sees description of django dungeon below header
        # and learns that she can create and play text adventures
        description = self.browser.find_element_by_id("id_welcome_description")
        self.assertIn("Create, play and share text adventures.", description.text)

        # She is invited to create a new adventure
        new_adventure_header = self.browser.find_element_by_id("id_new_adventure_header")
        self.assertIn("Create your own adventure", new_adventure_header.text)

        # She clicks the button to create a new adventure
        with self.wait_for_page_load(timeout=10):
            self.browser.find_element_by_id("id_new_adventure_button").click()

        # This redirects her to a 'new adventure' page
        # that invites her to enter basic story info
        header = self.browser.find_element_by_tag_name('h1')
        self.assertEqual("New Adventure", header.text)

        # She types "Haunted House Mystery" into the "title" box
        inputbox = self.browser.find_element_by_id('id_adventure_title')
        inputbox.send_keys('Haunted House Mystery')

        # She clicks the 'save' button to save the adventure
        self.browser.find_element_by_id('id_save_button').click()

        # And is redirected to the 'edit' adventure page with the first
        # location of her new adventure loaded and the title of her adventure at the top
        self.wait_for_element_with_id('id_edit_adventure_header')
        edit_adventure_header = self.browser.find_element_by_id('id_edit_adventure_header')
        self.assertIn("Haunted House Mystery", edit_adventure_header.text)

        # the initial description has a default value explaining how to edit
        location_description = self.browser.find_element_by_id('id_location_description')
        default_description = "Players will begin the adventure in this room. To edit the description replace the text and click the 'save' button."
        self.assertIn(default_description, location_description.text)

        # She clicks 'save and quit' to save the starting room as is
        self.browser.find_element_by_id('id_save_and_quit_button').click()

        # She returns to the homepage to see if her game is playable
        self.wait_for_element_with_id('id_adventure_table') # Explicit wait
        table = self.browser.find_element_by_id('id_adventure_table')
        rows = table.find_elements_by_tag_name('tr')
        row_text = [item.text for item in rows]
        self.assertIn('Haunted House Mystery', row_text)

    def test_can_add_choices_to_adventure(self):
        # User opens browser and navigates to url
        self.browser.get(self.live_server_url)

        # User sees description of django dungeon below header
        # and learns that she can create and play text adventures
        description = self.browser.find_element_by_id("id_welcome_description")
        self.assertIn("Create, play and share text adventures.", description.text)

        # She is invited to create a new adventure
        new_adventure_header = self.browser.find_element_by_id("id_new_adventure_header")
        self.assertIn("Create your own adventure", new_adventure_header.text)

        # She clicks the button to create a new adventure
        with self.wait_for_page_load(timeout=10):
            self.browser.find_element_by_id("id_new_adventure_button").click()

        # This redirects her to a 'new adventure' page
        # that invites her to enter basic story info
        header = self.browser.find_element_by_tag_name('h1')
        self.assertEqual("New Adventure", header.text)

        # She types "Haunted House Mystery" into the "title" box
        inputbox = self.browser.find_element_by_id('id_adventure_title')
        inputbox.send_keys('Haunted House Mystery')

        # She clicks the 'save' button to save the adventure
        self.browser.find_element_by_id('id_save_button').click()

        # And is redirected to the 'edit' adventure page with the first
        # location of her new adventure loaded and the title of her adventure at the top
        self.wait_for_element_with_id('id_edit_adventure_header')
        edit_adventure_header = self.browser.find_element_by_id('id_edit_adventure_header')
        self.assertIn("Haunted House Mystery", edit_adventure_header.text)

        # the initial description has a default value explaining how to edit
        location_description = self.browser.find_element_by_id('id_location_description')
        default_description = "Players will begin the adventure in this room. To edit the description replace the text and click the 'save' button."
        self.assertIn(default_description, location_description.text)

        # she clicks the button below the description to add a choice
        self.browser.find_element_by_id('id_add_choice_button').click()

        # and sees a textfield appear to enter a new choice
        self.wait_for_element_with_id('id_field_choice_1')
        inputbox = self.browser.find_element_by_id('id_choice_field_1')
        inputbox.send_keys('Enter Dungeon')

        # she then clicks the follow button indicated by arrow icon and "save and follow" tooltip
        with self.wait_for_page_load(timeout=10):
            self.browser.find_element_by_id('id_follow_button_choice_1').click()
        # and is redirected to a new room with placeholder text
        location_description = self.browser.find_element_by_id('id_location_description')
        default_description = "This is a new location. Edit this text and add choices as necessary."
        self.assertIn(default_description, location_description.text)


    # Publish/Unpublish functionality

        ### The publish checkbox should be on the 'edit' page, not 'new' page
        ## She notices that the option 'Publish Adventure' is unchecked
        # checkbox = self.browser.find_element_by_id('id_publish_checkbox')
        # self.assertFalse(checkbox.is_selected(), "Publish checkbox is selected")

        ## She checks the button
        # checkbox.click()
        # self.assertTrue(checkbox.is_selected(), "Publish checkbox failed to select")




if __name__ == '__main__':
    unittest.main()
