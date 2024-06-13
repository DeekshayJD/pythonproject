def compose(f,g,x):
    return f(g(x))

print(compose(print,len,"helloworld"))




'''
name="deekshay jd"
names=name.split()
x=min(names,key=len)
print(x)
'''