import json
with open("data.json","r")as fo:
    try:
        object = json.load(fo)
        print(object)
    except FileNotFoundError:
        print("please check the name of file")
        