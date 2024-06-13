import requests
'''
payload={
    "name": "deeekshay",
    "job": "leader"
}
payload={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
payload={
    "name": "morpheus",
    "job": "api testing"
}
'''
payload={
    "name":"API"
}

#resp=requests.post("https://reqres.in/api/users",data=payload)
#resp=requests.post("https://reqres.in/api/register",data=payload)
#resp=requests.put("https://reqres.in/api/users/2",data=payload)
resp=requests.post("https://reqres.in/api/users/2",data=payload)
print(resp.json())
#print(resp.headers.get("content-Type"))
#print(resp.json()["token"])
assert resp.json()["name"]=="API"