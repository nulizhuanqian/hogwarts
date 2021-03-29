import allure


@allure.link("https://www.baidu.com",name='链接')
def test_with_link():
    print("这是一条加了链接的测试")
    pass

TEST_CASE_LINK = "https://fanyi.baidu.com/static/webpage/pluginPage.html"
@allure.testcase(TEST_CASE_LINK,'登录用例')
def test_with_testcase_link():
    print("这是一条测试用例的链接")
    pass

# pytest test_alluredemo_link_issue_case.py --allure-link-pattern=issue:https://www.baidu.com/{} --alluredir=./result/link
# 链接前会有一个bug符号，并为链接加一个140，https://www.baidu.com/140
@allure.issue('140','这是一个issue')
def test_with_issue_lik():
    print("这是一条测试用例的链接")
    pass