import requests
p={"pages":2}
response=requests.get("https://reqres.in/api/users?",params=p)
print(response)
print(response.url)
json=response.json()
print(json)
print(json["support"]["url"])
'''
response=requests.get("https://reqres.in/api/users?page=2")
json_response=response.json()
print(json_response)
print(json_response["total"])
assert json_response["total"]==12
print(json_response["per_page"])
assert json_response["per_page"]==6,"total pages count doesn't match"
print(json_response["data"][0]["email"])
#assert json_response["data"][0]["email"]=="michael.lawson@reqres.in"
assert (json_response["data"][0]["email"]).endswith("reqres.in")
print(json_response["data"][1])
print(json_response["data"][1]["email"])
print(json_response["data"][1]["last_name"])
assert (json_response["data"][1]["last_name"])!=None
'''