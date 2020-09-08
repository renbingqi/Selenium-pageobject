"""
Name:basepage.py
Author:Rex
Time:2020/9/1 22:28
Desc:基类封装页面对象中需要用到的基础方法
"""
import time

from selenium.webdriver.common.by import By

from Utils.driver.driver import Driver
from Log.mylog import Logger
mylog=Logger().my_log()
class BaseObject(Driver):
    def __init__(self, driver):
        # 实例化一个driver
        super().__init__()
        self.driver=driver
        date=time.time()
        self.fimename="{}.jpg".format(date)



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
            mylog.info("{}元素定位错误".format(ele))
            self.driver.getScreenshotAs(self.fimename)

    #点击元素
    def click_ele(self,*ele):
        """

        :param ele:元素定位方式
        :return:
        """
        try:
            self.find_ele(*ele).click()
        except:
            mylog.info("{}点击失败".format(str(ele)))
            self.driver.getScreenshotAs(self.fimename)

    #输入文字
    def send_keys(self,*ele,keys):
        """

        :param ele:元素定位方式
        :param keys: 需要输入的文字
        :return:
        """
        try:
            self.find_ele(*ele).send_keys(keys)
        except:
            mylog.info("{}输入文字失败".format(str(ele)))
            self.driver.getScreenshotAs(self.fimename)

    #等待元素
    def implicity_wait(self):
        try:
            self.driver.implicitly_wait(10)
        except:
            mylog.info("等待超时")
            self.driver.getScreenshotAs(self.fimename)

    #浏览器前进
    def forword(self):
        try:
            self.driver.forward()
        except:
            mylog.info("浏览器前进失败")
            self.driver.getScreenshotAs(self.fimename)

    def get_sceenshot(self):
        try:
            date=time.time()
            self.driver.get_screenshot_as_file(filename="../screenshot/{}.png".format(date))
        except:
            mylog.info("截屏失败")






# runner=BaseObject()
# runner.open_brower()

