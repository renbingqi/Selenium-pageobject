"""
Name:testLogin.py
Author:Rex
Time:2020/9/2 21:45
Desc:登录测试
"""
import time

from PageObject.LoginPage import LoginPage
import unittest
from Utils.driver.driver import Driver
from ddt import ddt,data,unpack



@ddt
class TestLogin(Driver):
    @data(*[('admin','admin'), ('vivalnk','vivalnk')])
    @unpack
    def test_login(self,username,password):
        """

        :param username:登录用户名
        :param password: 登录密码
        :return: null
        """
        #实例化LoginPage页面对象
        self.loginpage=LoginPage(self.browser)
        #打开登录页面
        self.browser.get("http://localhost:3000/#/login?redirect=%2F")
        self.loginpage.login(username=username,password=password)
        #登录成功跳转到Home页面，断言登录是否成功
        self.assertEqual(self.browser.title,"Home")


if __name__=="__main__":
    unittest.main()
