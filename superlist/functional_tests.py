# This kind of test often contains a user story (steps -> accomplish sth)
# also, it can be called as [~Terminology]
#   functional test     what does it do
#   acceptance test     test from the point of user
#   end-to-end test     does it satisfy my need
#   black box  test     knows nothing about internal stuff
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    SAFARI_DRIVER = "/usr/bin/safaridriver"
    FIREFOX_DRIVER = "/usr/local/bin/geckodriver"

    def setUp(self):
        # Normally this will run perfectly without a fuss.
        # For me I need to dl a new one, since I'm using the Dev edition :(
        self.browser = webdriver.Safari(executable_path=self.SAFARI_DRIVER)

    def tearDown(self):
        self.browser.quit()  # For safari, you must use 'quit()'

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Andrew has heard about a cool new todo-app.
        # She decided to check out its homepage.
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention TODO-list
        self.assertIn("TODO-list", self.browser.title)

        header_text = self.browser.find_element_by_name("h1").text()
        self.assertIn("TODO-list", header_text)

        # She is invited to write her first todo item.
        # She types "Learn TDD with Django & Selenium" into a text box.
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a TODO item")

        inputbox.send_keys("Learn TDD with Django")

        # When she hits 'Enter', the page updates, and now the page
        # list '<1> Learn TDD with Django & Selenium'
        inputbox.send_keys(Keys.ENTER)
        time.sleep(0.5)

        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(any(row.text == "1: Learn TDD with Django" for row in rows))

        # She then inputs another TODO item, then hits 'Enter',
        # the page updates again, now it shows both the items she added.
        self.fail("Finish the test!")  # Optional (behaves like raise Exception)

        # Now she wonders whether the site will remember her list. Then
        # she sees the sites geenrated a unique URL for her -- there'd be
        # some explanatory text to that effect.

        # She visits that URL -- her TODO list is still there.

        # Then she go back to sleep, peace.


if __name__ == "__main__":
    unittest.main(warnings="ignore")
