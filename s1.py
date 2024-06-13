string=input("enter string :-")
char=input("enter character :-")
index,count=0,0
while(index<len(string)):
    if string[index]==char:
        count+=1
    index+=1
print(f"{char}=={count}")
