from login import login
import time
from selenium import webdriver

user,password = login()

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('http://www.twitter.com/login')
time.sleep(1.5)
userfield = driver.find_element_by_css_selector("input[type='text']")
userfield.send_keys(user)
passwordfield = driver.find_element_by_css_selector("input[type='password']")
passwordfield.send_keys(password)
passwordfield.submit()

input("Press Enter to quit")

driver.quit()
