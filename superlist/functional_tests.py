# This kind of test often contains a user story (steps -> accomplish sth)
# also, it can be called as [~Terminology]
#   functional test     what does it do
#   acceptance test     test from the point of user
#   end-to-end test     does it satisfy my need
#   black box  test     knows nothing about internal stuff
from selenium import webdriver

# Normally this will run perfectly without a fuss.
# For me I need to download a new one, since I'm using the Dev edition :(
browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
browser.get('http://localhost:8000')

# Andrew has heard about a cool new todo-app. 
# She decided to check out its homepage.

try:
    assert 'TODO-list' in browser.title
except AssertionError: 
    raise
else:
    print('Unknown errors OR everything is fine')
finally:
    browser.close()  # Close instantly

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

