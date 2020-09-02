"""
Name:basepage.py
Author:Rex
Time:2020/9/1 22:28
Desc:基类封装页面对象中需要用到的基础方法
"""
from selenium.webdriver.common.by import By

from Utils.driver.driver import Driver
class BaseObject(Driver):
    def __init__(self,driver):
        # 实例化一个driver
        self.driver=driver


    def open_brower(self,url):
        """

        :param url:要打开的网址
        :return:
        """
        self.driver.get(url=url)
        return self.driver

    #查找元素
    def find_ele(self,*ele):
        """

        :param ele:传入元素定位方式
        :return:元素对象
        """
        try:
            return self.driver.find_element(*ele)

        except:
            print("元素定位错误")

    #点击元素
    def click_ele(self,*ele):
        """

        :param ele:元素定位方式
        :return:
        """
        self.find_ele(*ele).click()

    #输入文字
    def send_keys(self,*ele,keys):
        """

        :param ele:元素定位方式
        :param keys: 需要输入的文字
        :return:
        """
        self.find_ele(*ele).send_keys(keys)

    #等待元素
    def implicity_wait(self):
        self.driver.implicitly_wait(10)

    #浏览器前进
    def forword(self):
        self.driver.forward()






# runner=BaseObject()
# runner.open_brower()

