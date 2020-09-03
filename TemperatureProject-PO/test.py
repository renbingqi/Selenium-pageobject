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

# browser=webdriver.Chrome()
# print(browser)
# browser.get("http://localhost:3000/#/login")
# username=browser.find_element(By.XPATH,"/html/body/section/main/form/div[1]/div/div/input")
# password=browser.find_element(By.XPATH,"/html/body/section/main/form/div[2]/div/div/input")
# submit=browser.find_element(By.XPATH,"/html/body/section/main/form/div[3]/div/button")
# username.send_keys("admin")
# password.send_keys("admin")
# submit.click()
# time.sleep(5)
# browser.forward()
# print(browser.title)
jsonfile = open('G:\本地仓库\TemperatureProject-PO\Config\driver.yaml')
dict_file=yaml.full_load(jsonfile)
print(dict_file)
# driver_name=dict_file["browser"]["driver"]
# longin_data=dict_file["logindata"]
# print(driver_name)
# print(longin_data)







