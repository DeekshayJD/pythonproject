import json
numbers=[1,2,3,4,5]
with open("data.json","w")as fo:
    json.dump(numbers,fo)
    