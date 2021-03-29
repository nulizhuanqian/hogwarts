import requests
from hamcrest import assert_that, equal_to
from jsonpath import jsonpath
class TestDemo:
    def test_get(self):
        r=requests.get("https://httpbin.testing-studio.com/get")
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
    def test_query(self):
        payload={
            "level": 1,
            "name": "tom"
        }
        r=requests.get('https://httpbin.testing-studio.com/get',params=payload)
        print(r.text)
        print(r.status_code)
    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "tom"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        print(r.status_code)
    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "tom"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        print(r.status_code)
        assert r.json()["json"]["level"]==1

# json响应断言
    def test_hogwarts_json(self):

        r = requests.get('https://ceshiren.com/categories.json')
        assert r.status_code==200
        assert r.json()["category_list"]["categories"][0]['name']== '开源项目'
# jsonpath
    def test_jsonpath(self):
        r = requests.get('https://ceshiren.com/categories.json')
        assert r.status_code == 200
        assert jsonpath(r.json(),'$..name')[0]=='开源项目'
# hamcrest的assert_that断言
    def test_hamcrest(self):
        r = requests.get('https://ceshiren.com/categories.json')
        assert r.status_code == 200
        assert_that(r.json()["category_list"]["categories"][0]['name'],equal_to('开源项目'))


    def test_hearder(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={"h":"header demo"})
        print(r.text)
        print(r.status_code)
        print(r.json())
        assert r.status_code==200
        assert r.json()['headers']['H'] == "header demo"
