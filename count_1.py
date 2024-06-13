count=1
def do_this():
    global count
    for i in (1,2,3):
        count+=i
do_this()
print(count)

a=[1,2,3,4,5]
#print(a[3:10])

print(a[-1:-10])