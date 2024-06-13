import re
result=re.finditer("[0-9]","ab32dec")
for m in result:
    print(m.group(),end="")

