s="deekshay is good boy"
word=s.split()
l1=[]
i=len(word)-1
while i>=0:
    l1.append(word[i][::-1])
    i=i-1
output=" ".join(l1)
print(output)
