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

class Driver(object):
    def get_driver_name(self):
        jsonfile = open('G:\本地仓库\TemperatureProject-PO\Config\driver.json', 'r')
        driver_name = json.load(jsonfile)['driver']
        return driver_name

    def get_driver(self,driver_name):
        if driver_name=="Chrome":
            brower=webdriver.Chrome()
            return brower
        else:
            brower=webdriver.Firefox()
            return brower

    def main(self):
        driver_name=self.get_driver_name()
        brower=self.get_driver(driver_name)
        # brower.get(url="https://www.baidu.com")
        return brower

if __name__=="__main__":
    runner=Driver()
    runner.main()
