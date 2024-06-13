#count string
index,count=0,0
string=input("enter string :-")
char=input("enter character to count number of times")
while(index<len(string)):
    if string[index]==char:
        count+=1
    index+=1

print(f"{char} repated {count} times")