data="hai good morning"
with open("d.txt","w")as fo:
    fo.write(data)

with open("d.txt","r")as fo:
    text=fo.readline()
    print(text)