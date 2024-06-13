#List1= [“W”, “a”, “w”,”b”]List2 = [“e”, “ “,”riting”,”log”]
#output=[‘We’, ‘a ‘, ‘writing’, ‘blog’]
list1=["w","a","w","b"]
list2=["e"," ","riting","log"]

output=[i+j for i,j in zip(list1,list2)]
print(output)