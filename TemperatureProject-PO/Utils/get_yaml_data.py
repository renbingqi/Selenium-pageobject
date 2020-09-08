"""
Name:get_yaml_data.py
Author:Rex
Time:2020/9/7 21:22
Desc:从Config下的data.yaml文件中获取数据
"""
import yaml
class GetData():
    def __init__(self):
        self.file = open("../Config/data.yaml", "r", encoding="utf-8")
        self.data = yaml.load_all(self.file, Loader=yaml.Loader)
        self.data_list=[]
        self.get_data_list()

        # self.it = iter(self.data)
    # 获取driver的名字
    def get_data_list(self):
        for data in self.data:
            self.data_list.append(data)


    def get_driver(self):
        return self.data_list[0]["driver"]
    # 获取登录的数据（用户名 密码）
    def get_login_data(self):
        return self.data_list[1]




if __name__=="__main__":
    runner=GetData()
    runner.get_driver()
    runner.get_login_data()