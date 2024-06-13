import re
spChar = "!@#$%^&*()"
count=re.sub("[\W]","",spChar)
print(len(count))