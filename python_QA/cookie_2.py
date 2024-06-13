import requests
jar=requests.cookies.RequestsCookieJar()
jar.set("tasty_cookies","yum",domain="httpbin.org",path="/cookies")
url="https://httpbin.org/cookies"
r=requests.get(url,cookies=jar)
print(r.text)