vowel=["a","e","i","o","u"]
string="programing"
l1=[]
count=0
for i in string:
    if i in vowel:
     if i not in l1:
        l1.append(i)
     count+=1
print(f"{l1}, {count}element with number of times repeated")




