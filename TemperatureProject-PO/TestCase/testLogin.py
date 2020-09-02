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
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver=Driver().main()  #得到一个浏览器对象
        self.driver.maximize_window()
        self.loginpage=LoginPage(self.driver) #实例化一个LoginPage对象并把浏览器对象传过去
        self.loginpage.open_brower(url="http://localhost:3000/#/login")#打开登录页面

    @data(*[("admin","admin"),("vivalnk","vivalnk")])
    @unpack
    def test_login(self,username,password):
        self.loginpage.login(username=username,password=password)
        self.assertEqual(self.driver.title,"Home")

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()
