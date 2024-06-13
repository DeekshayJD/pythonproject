d={"a":[1],"b":[1,2],"c":[],"d":[]}
#output="a":[1],"b":[1,2]
#for a,b in d.item):
print(f"valve of a id{d["a"]} and value of b is{d["b"]}")

d = {"a": [1], "b": [1, 2], "c": [], "d": []}

output = {key: value for key, value in d.items() if value}
print(output)









'''

for x in range(10):
    if x==5:
        continue

    print(x)

def f(x):
 return x**2
print(f(2))
'''