"""
Name:test.py
Author:Rex
Time:2020/9/1 21:57
Desc:测试
"""
#读取driver.json文件
from selenium import webdriver
browser=webdriver.Chrome()
print(browser)
browser.get("https://www.baidu.com")






