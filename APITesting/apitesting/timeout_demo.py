import requests
resp=requests.get("https://httpbin.org/delay/5",timeout=10)
print(resp.status_code)