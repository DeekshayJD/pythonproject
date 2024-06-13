import re

string = "C O D E"
#spaces = re.compile(r'\s+')
spaces=re.compile("\s+")

result = re.sub(spaces, '', string)
print(result)
