import re,urllib
import urllib.request
u=urllib.request.urlopen("https://www.redbus.in/info/contactus")

text=u.read()
numbers=re.findall("[0-9-]{7}[0-9-]+",str(text),re.I)
for n in numbers:
 print(n)