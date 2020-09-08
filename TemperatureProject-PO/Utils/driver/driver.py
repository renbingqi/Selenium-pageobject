"""
Name:driver.py
Author:Rex
Time:2020/9/1 21:46
Desc:读取driver json文件
创建对应的driver对象
通过调用main函数直接获取brower对象
"""
import json

from selenium import webdriver
import unittest
from Utils.get_yaml_data import GetData
class Driver(unittest.TestCase):
    #实例化一个getdata对象
    get_driver_data=GetData()
    def setUp(self):
        self.driver_name=self.get_driver_name()
        self.browser=self.get_driver(self.driver_name)
        self.browser.maximize_window()
    #从本地配置文件中读取测试用浏览器名字
    def get_driver_name(self):
        return self.get_driver_data.get_driver()

    def get_driver(self,driver_name):
        if driver_name=="Chrome":
            brower=webdriver.Chrome()
            return brower
        else:
            brower=webdriver.Firefox()
            return brower
    # def test1(self):
    #     print("1")


    def tearDown(self):
        self.browser.quit()

if __name__=="__main__":
    unittest.main()
