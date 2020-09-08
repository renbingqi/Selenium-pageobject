"""
Name:test.py
Author:Rex
Time:2020/9/1 21:57
Desc:测试
"""
#读取driver.json文件
import json
import time
import yaml

from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
browser.get("http://localhost:3000/#/login")
browser.maximize_window()
date=time.time()
browser.get_screenshot_as_file(filename="./screenshot/{}.png".format(date))









