import requests

# 使用headers自定义传递Cookie
class TestCookie:
    def test_demo(self):
        url="http://httpbin.ceshiren.com/cookies"
        # Cookie首字母要大写
        header = {"Cookie":"hogwarts=school",
                  'User-Agent': 'hogwarts'
                  }
        r = requests.get(url=url,headers=header)
        print(r.request.headers)


    # 使用cookies传递参数
    def test_demo2(self):
        url="http://httpbin.ceshiren.com/cookies"
        # Cookie首字母要大写
        header = {
                  'User-Agent': 'python-requests/2.25.1'
                  }
        # 传递多条cookie
        cookie_data={"hogwarts":"scholl",
                     "teacher":"AD"

                     }
        r = requests.get(url=url,headers=header,cookies=cookie_data)
        print(r.request.headers)