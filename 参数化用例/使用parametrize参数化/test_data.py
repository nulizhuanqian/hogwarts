import pytest


class TestData:
    # 使用string参数化'a,b'或者"a,b"
    @pytest.mark.parametrize('a,b',[
        (10,20),
        (10,5),
        (3,9)

    ])
    def test_data(self,a,b):
        print(a+b)

    # 使用元组tuple参数化
    @pytest.mark.parametrize(("a","b"),[
        (10,20),
        (10,5),
        (3,9)

    ])
    def test_data1(self,a,b):
        print(a+b)

    # 使用列表参数化
    @pytest.mark.parametrize(["a","b"],[
        (10,20),
        (10,5),
        (3,9)

    ])
    def test_data2(self,a,b):
        print(a+b)

    # 多次使用parametrize，如下生成了2*3=6种结合，pytest会生成6条测试用例
    @pytest.mark.parametrize("x",[1,2])
    @pytest.mark.parametrize("y",[8,9,10])
    def test_data2(self,x,y):
        print(f"测试数据组合x:{x},y:{y}")
