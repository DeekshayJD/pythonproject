import requests

response=requests.get("https://reqres.in/api/unknown/2")
json_resonse=response.json()
print(json_resonse)
print(json_resonse["data"]["id"])
assert json_resonse["data"]["id"]==3,"does not match"