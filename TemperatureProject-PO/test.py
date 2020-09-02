"""
Name:test.py
Author:Rex
Time:2020/9/1 21:57
Desc:测试
"""
#读取driver.json文件
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
print(browser)
browser.get("http://localhost:3000/#/login")
username=browser.find_element(By.XPATH,"/html/body/section/main/form/div[1]/div/div/input")
password=browser.find_element(By.XPATH,"/html/body/section/main/form/div[2]/div/div/input")
submit=browser.find_element(By.XPATH,"/html/body/section/main/form/div[3]/div/button")
username.send_keys("admin")
password.send_keys("admin")
submit.click()
time.sleep(5)
browser.forward()
print(browser.title)







