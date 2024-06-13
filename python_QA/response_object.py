import requests
baseUrl="https://api.github.com/events"

#for printing response object

def printData(res):
    #print(res.json())
    #print(res.status_code)
    #print(res.text)
    #print(type(res.text))
    #print(res.headers)
    #print(res.headers['Content-Type'])
    print(res.raw.read(10))
try:
    res=requests.get(baseUrl,stream=True)
    print(res.url)
    #print(res.status_code)
    printData(res)

except requests.exceptions.HTTPError as err:
    raise SystemExit(err)