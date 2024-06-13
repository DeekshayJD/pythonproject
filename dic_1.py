#fact _of num
def fibonaccii():
    a,b=0,1
    while True:
        a,b=b,a+b
    yield a

fib=fibonaccii()
for i in range(19):
    print(next(fib))



'''
dic=eval(input("enter dictinory:-"))
s=sum(dic.values())
print(sum)

'''

def occurence(words,vowels):
    dic={}
    for i in words:
        if i in vowels:
         dic[i]=dic.get(i,0)+1

    for k,v in dic.items():
        print(k,"=",v)

words="deekshay"
vowels={"a","e","i","o","u"}
occurence(words,vowels)
