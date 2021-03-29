import pytest
"""
pytest test_feature_story.py --alluredir=./result/2
方法一
allure serve ./result/3    生成在线的测试报告，使用默认浏览器打开

方法二  
allure generate ./result/2 -o ./report/2/ --clean
allure open -h 127.0.0.1 -p 8883 ./report/2 

"""

def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')

