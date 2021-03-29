import time

import allure
import pytest
import selenium
import yaml
from selenium import webdriver

@allure.testcase("https://ceshiren.com/t/topic/7178")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1',yaml.safe_load(open("./data/baidu.yaml")))
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        driver=webdriver.Chrome()
        driver.get("https://www.baidu.com/")
        driver.maximize_window()
    with allure.step(f"输入搜索词：{test_data1}"):
        driver.find_element_by_id("kw").send_keys(test_data1)
        # time.sleep(2)
        driver.find_element_by_id("su").click()
        # time.sleep(2)
    with allure.step("保存图片"):
        driver.save_screenshot("./result/baidu.png")
        allure.attach.file("./result/baidu.png",attachment_type=allure.attachment_type.PNG)
    with allure.step("关闭浏览器"):
        driver.quit()

