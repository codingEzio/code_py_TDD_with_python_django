# This kind of test often contains a user story (steps -> accomplish sth)
# also, it can be called as [~Terminology]
#   functional test     what does it do
#   acceptance test     test from the point of user
#   end-to-end test     does it satisfy my need
#   black box  test     knows nothing about internal stuff
import unittest
from selenium import webdriver


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

        # Optional (behaves like raise Exception)
        self.fail("Finish the test!")

        # She is invited to write her first todo item.
        # She types "Learn TDD with Django & Selenium" into a text box.

        # When she hits 'Enter', the page updates, and now the page
        # list '<1> Learn TDD with Django & Selenium'

        # She then inputs another TODO item, then hits 'Enter',
        # the page updates again, now it shows both the items she added.

        # Now she wonders whether the site will remember her list. Then
        # she sees the sites geenrated a unique URL for her -- there'd be
        # some explanatory text to that effect.

        # She visits that URL -- her TODO list is still there.

        # Then she go back to sleep, peace.


if __name__ == "__main__":
    unittest.main(warnings="ignore")
