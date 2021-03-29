import pytest


def func(x):
    return x+1

# 参数化
@pytest.mark.parametrize('a,b',[
    (1,2),
    (10,20),
    ('a','a1')

])
def test_answer(self,a,b):
    assert func(a) == b

def test_answer1():
    assert func(4) == 5

#加上这个装饰后可以将这个函数以参数的形式传到方法里，这个方法就会先执行login，再去执行自身的用例步骤
@pytest.fixture()
def login():
    print("登录操作")
    username = 'Tom'
    return username

class  TestDemo:
    # 类中不能有init方法，否则这个类不能被pytest识别
    def test_a(self,login):
        print(f"a username={login}")
    def test_b(self):
        print("b")
    def test_c(self,login):
        print(f"c login={login}")
    # 没有以test_开头，不能被pytest识别
    # def c(self):
    #     print("c")

# 使用Python解释器执行pytest需要入口函数，pytest.main([])中的参数与命令行中用pytest相同，既可以直接右键run，也可以在命令行中执行python -文件名.py
# pytest 文件名.py
# pytest 文件名.py::类名
# pytest 文件名.py::类名::方法名
# if __name__=='__main__':
#
#     pytest.main(['test_a.py'])
if __name__=='__main__':

    pytest.main(['test_a.py::TestDemo','-v'])
# if __name__=='__main__':
#
#     pytest.main(['test_a.py::TestDemo::test_a','-v'])
