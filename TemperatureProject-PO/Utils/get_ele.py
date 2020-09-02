"""
Name:get_ele.py
Author:Rex
Time:2020/9/2 21:27
Desc:获取元素
"""
import json
class GetEle():
    def get_login_ele(self):
        file= open("G:\本地仓库\TemperatureProject-PO\Config\login.json",'r')
        dict_login_ele=json.load(file)
        print(dict_login_ele['username'])
        return dict_login_ele



if __name__=="__main__":
    getdata=GetEle()
    getdata.get_login_ele()