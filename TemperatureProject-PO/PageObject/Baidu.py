"""
Name:Baidu.py
Author:Rex
Time:2020/9/1 22:45
Desc:
"""
from Base.basepage import BaseObject


class Baidu(BaseObject):
    def open(self):
        self.open_brower()


runner=Baidu()
runner.open()

