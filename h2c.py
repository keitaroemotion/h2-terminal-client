#!/usr/bin/env python3

#
# https://chromedriver.storage.googleapis.com/index.html
# download chromedriver matches the Chrome Browser version
# you are currently using.
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def finish():
    txt = input('quit? [y/n]')
    if(txt == 'y' or txt == 'Y'):
      driver.close()
    else:
      finish()

driver = webdriver.Chrome()
driver.get('http://localhost:8080/dbconsole/login.jsp')
driver.find_element_by_xpath("//input[@type='submit']").click()
driver.switch_to_frame("h2query")
time.sleep(1)
elem = driver.find_element_by_xpath("//textarea[@id='sql']")
elem.clear()
elem.send_keys("select * from fixed_data")
elem = driver.find_element_by_xpath("//input[@value='Run']").click()
time.sleep(3)
finish()
