#! python3
# 2048.py - auto 'up right down left'

import bs4
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://gabrielecirulli.github.io/2048/')

html = browser.find_element_by_tag_name('body')
while True:
    html.send_keys(Keys.UP)
    html.send_keys(Keys.RIGHT)
    html.send_keys(Keys.DOWN)
    html.send_keys(Keys.LEFT)