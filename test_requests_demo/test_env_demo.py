from unittest import TestCase

from test_requests_demo import env_demo


class TestApi(TestCase):
    data = {
        "method":"get",
        "url":"http://127.0.0.1:9999/demo.txt",
        "headers":None
    }
    def test_send(self):
        api = env_demo.Api()
        print(api.send(self.data).text)

