import selenium


def add(x,y):
    return x+y
"""
1、pytest test_alluredemo.py --alluredir=./result/1
2、allure serve ./result/1   在线看报告，使用默认浏览器打开
3、allure generate ./result/2 -o ./report/2/ --clean ./report/2 将报告生成到/report/2路径下
4、allure open -h 127.0.0.1 -p 8883  启动一个本地的服务来打开/report/2目录下的报告

"""
def test_add():

    assert add(1,10) == 11
    assert add(1, 1) == 2
    assert add(1, 99) == 100

class TestClass:
    def test_one(self):
        x="this"
        assert "h" in x
    def test_two(self):

        x = "hello"
        assert  hasattr(x,"check")

