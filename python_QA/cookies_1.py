import requests

url="https://httpbin.org/cookies"
cookies=dict(cookies_are="working",cookies_are1="working")
r=requests.get(url,cookies=cookies)
print(r.text)