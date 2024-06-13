import requests
baseURL="https://swapi.dev/api/people/"
queryparams={"search":"r2"}
specificresources="2"
#for response object validation
def validation(res):
    assert res.status_code==200,"fail"

    assert res.headers["content-Type"]=="application/json","Fail"

try:
    #get request with query parameter
    res=requests.get(baseURL,params=queryparams)
    print(res.url) #for checking the url
    res.raise_for_status() #check if any http error occured  and raise exception
    validation(res)

except requests.exceptions.HTTPError as err:
    raise SystemExit(err)
try:
    #get request with specific resource(2)
    res = requests.get(baseURL+specificresources)
    print(res.url)  # for checking the url
    res.raise_for_status()  # check if any http error occured  and raise exception
    validation(res)
except requests.exceptions.HTTPError as err:
    raise SystemExit(err)

