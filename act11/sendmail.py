#! python3
# sendmail.py - sendmail by CMD
# 该脚本未完成，需要根据html查询对应字段以获取提交信息。需要深挖JS信息

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys


# if len(sys.argv) != 3:
#     print('please input mail address and content')
#     exit()
browser = webdriver.Firefox()
browser.get('http://exmail.qq.com/login')
user = browser.find_element_by_id('inputuin')
user.send_keys('account@fairlinkcentury.com')
password = browser.find_element_by_id('pp')
password.send_keys('password')
password.submit()

# browser.get('https://exmail.qq.com/cgi-bin/frame_html?sid=EQyaA2Kr2yhJfyx0,7&r=1af1177983567fa08d2d2bcab78ae604')
# receiver = browser.find_element_by_class_name('addr_base')
# receiver.send_keys('daize.song@fairlinkcentury.com')