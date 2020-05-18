#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

def finish():
    txt = input('quit? [y/n]')
    if(txt == 'y' or txt == 'Y'):
      driver.close()
    else:
      finish()

args = sys.argv[1:]
if (len(args) == 0):
    print('\nyou need argument.\n')
    sys.exit()

query = ';'.join(args)

print("query: {}".format(query))
driver = webdriver.Chrome()
driver.get('http://localhost:8080/dbconsole/login.jsp')
driver.find_element_by_xpath("//input[@type='submit']").click()
driver.switch_to.frame("h2query")
time.sleep(1)
elem = driver.find_element_by_xpath("//textarea[@id='sql']")
elem.clear()
elem.send_keys(query)
elem = driver.find_element_by_xpath("//input[@value='Run']").click()
#
# TODO: later...
#
# driver.switch_to.frame("h2result")
# elem = driver.find_elements_by_class("sortHeader")
time.sleep(3)
finish()
