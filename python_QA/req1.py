import requests

#r=requests.get("https://api.github.com/events",stream=True)
url="https://api.github.com/some/endpoint"
headers={"user-agent":"my-app/0.0.1"}
r=requests.get(url,headers=headers)
print(r.url)
#print(r.raw)
#print(r.raw.read(10))
#print(r.text)
#print(r.json())
#r.encoding="ISO-8859"
#print(r.encoding)
#print(r.content)


'''

payload={"key1":"value1","key2":"value2"}
r=requests.get("https://httpbin.org/get",params=payload)
print(r.url)

payload={"key1":"value1","key2":["value2","value3"]}
r=requests.get("https://httpbin.org/get",params=payload)
print(r.url)


'''

