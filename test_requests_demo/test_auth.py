import requests
from requests.auth import HTTPBasicAuth


def test_auth():
    r=requests.get(url= "http://httpbin.ceshiren.com/basic-auth/banana/123",
                 auth=HTTPBasicAuth("banana","123"))
    print(r)
    print(r.text)