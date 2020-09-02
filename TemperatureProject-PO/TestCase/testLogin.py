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
# @ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver=Driver().main()
        self.driver.maximize_window()
        self.loginpage=LoginPage(self.driver)
        self.loginpage.open_brower(url="http://localhost:3000/#/login")#打开登录页面
    # @data()
    # @unpack
    def test_login(self):
        self.loginpage.login(username="admin",password="admin")
        self.assertEqual(self.driver.title,"Home")

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()
