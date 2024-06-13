vowels=['a','e','i','o','u']
words=input("Enter the word to search for vowels: ")
output=[]
for word in words:
    if word in vowels:
        if word not in output:
            output.append(word)
print(f"unique vowels are{output} with thier length{len(output)}")








words="the quick brown fox jumps over the lazy dog".split()
print(words)
res=[[w.upper(),len(w),id(w)] for w in words]
print(res)







n = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(len(n[1]))
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j],end=" ")
    print()











x=[10,20,30,40]
y=x.copy()
y[1]=100
print(id(x))
print(id(y))