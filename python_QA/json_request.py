import json

import requests
url="https://httpbin.org/post"
payload={"some":"data"}
r=requests.post(url,data=json.dumps(payload))
#r=requests.post(url,data=json.dump(payload))
print(r.content)