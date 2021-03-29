"""
在请求之前，对请求的url进行替换
1、需要二次封装requests，对请求进行定制化
2、将请求的结构体url从一个写死的IP地址改为一个（任意的）域名
3、使用一个env配置文件存放各个环境的配置信息
4、然后将请求结构体中的url替换为‘env’配置文件中个人选择的url
5、将env配置文件使用yaml进行管理
"""
import requests
import yaml


class Api:
    # data = {
    #     "method":"get",
    #     "url":"http://127.0.0.1:9999/demo.txt",
    #     "headers":None
    # }
    env = yaml.safe_load(open("env.yaml"))

    def send(self,data:dict):
        # 替换                                                   self.env["test-studio"]["dev"]
        data["url"] = str(data["url"]).replace("testing-studio",self.env["test-studio"][self.env["default"]])
        r = requests.request(method=data["method"],url=data["url"],headers=data["headers"])
        return r