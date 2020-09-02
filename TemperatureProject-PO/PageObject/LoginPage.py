"""
Name:LoginPage.py
Author:Rex
Time:2020/9/2 21:11
Desc:登录页面
"""
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from Base.basepage import BaseObject
from Utils.get_ele import GetEle
class LoginPage(BaseObject):
    username=eval(GetEle().get_login_ele()["username"])
    password=eval(GetEle().get_login_ele()["password"])
    submit=eval(GetEle().get_login_ele()["submit"])

    # def changeLanguage(self):
    #     pass
    #
    def login(self,username,password):
        self.send_keys(*self.username,keys=username)  #输入用户名
        self.send_keys(*self.password,keys=password)  #输入密码
        self.click_ele(*self.submit) #点击登录
        time.sleep(1)
        self.forword()#浏览器前进

if __name__=="__main":
    driver=webdriver.Chrome()
    login=LoginPage(driver)

