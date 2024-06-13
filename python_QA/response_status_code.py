import requests
r=requests.get("https://httpbin.org/post")
print(r.status_code)
print(r.status_code==requests.codes.ok)
print(requests.codes.ok)