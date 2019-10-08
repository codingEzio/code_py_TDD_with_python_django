from selenium import webdriver

# Normally this will run perfectly without a fuss,
# I'm using the Dev edition
browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
