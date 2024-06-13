dic={"name":"deekshay","age":25}
print(dic.keys())
print(dic.values())
print(dic.get("name"))
dic["pno"]=81976834
for key ,value in dic.items():
    print(key,value)


print("_"*30)

l1=[10,"RS",["c","cpp","python"],[20,30,4],"ANU"]
print(l1[2])
print(l1[2][1:3])


s="deekshay"
print(s[-1])
l1=[1,3,4,5,2]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.sort(reverse=True)
print(l1)