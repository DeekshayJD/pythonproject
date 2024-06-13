import requests
r=requests.get("https://httpbin.org")
print(r.headers)
print(r.headers["content-Type"])
