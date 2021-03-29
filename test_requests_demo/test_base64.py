import base64
import json

import requests

# python -m http.server 9999
def test_encode():
    url = "http://127.0.0.1:9999/demo.txt"
    r= requests.get(url=url)
    res = json.loads(base64.b64decode(r.content))
    print(res)
class ApiRequest:
    def send(self,data:dict):
        res = requests.request(data["method"],data["url"],headers=data["headers"])
        if data["encoding"]=="base64":
            return json.loads(base64.b64decode(res.content))
        # 把加密后的响应值发送给第三方服务，让第三方去做解密然后返回
        elif data["encoding"]=="private":
            return requests.post("url",data = res.content)
class TestApiRequest:

    req_data = {
        "method":"get",
        "url":"http://127.0.0.1:9999/demo.txt",
        "headers":None,
        "encoding":"base64"
    }
    def test_send(self):
        ar=ApiRequest()
        print(ar.send(self.req_data))