import requests
#baseUrl="http://httpbin.org/post"
baseUrl="https://eov4skvvi669fd0.m.pipedream.net"
#method1 single file upload

#file={"file1":open("sample1.csv","rb")}

#method2 multiple file upload

file=[("file1",("sample1.csv",open("sample1.csv","rb"),"csv"))
("file2",("sample2.csv",open("sample2.csv","rb"),"csv"))
      
      ]


#for response object validation
def validation(res):
    assert res.status_code==200,"fail"
try:
    res=requests.post(baseUrl,files=file)
    print(res.url)
    res.raise_for_status()
    validation(res)
except requests.exceptions.HTTPError as err:
    raise SystemExit(err)
