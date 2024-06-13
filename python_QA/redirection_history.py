'''
import requests
r=requests.get("https://facebook.com",allow_redirects=True)

print(r.url)
print(r.history)
print(r.status_code)
print(len(r.history))

'''
import requests

# Sending a GET request to a URL that redirects
response = requests.get("http://httpbin.org/redirect/3")

# Checking the final URL after redirects
final_url = response.url

# Checking the history of redirects
redirect_history = response.history

# Printing the final URL and redirect history
print("Final URL after redirects:", final_url)
print("Redirect history:")
for redirect_response in redirect_history:
    print("Redirected from:", redirect_response.url)
    print("Redirect status code:", redirect_response.status_code)
