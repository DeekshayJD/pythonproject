def bracketbalance(str):
    count=0
    ans=False
    for i in str:
        if i in "{" or i in "(" or i in "[":
            count+=1
        elif i in "}"or i in ")" or i in "]":
            count-=1
        if count<0:
            return ans
        if count==0:
            return not ans
    return ans
print(bracketbalance("{[()}]"))