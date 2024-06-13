def find_missing_num(lst):
    n=len(lst)+1
    total_sum=n*(n+1)//2
    actual_sum=sum(lst)
    missing_num=total_sum-actual_sum
    return missing_num







lst=[1,2,3,5,6,7,8,9]
print(find_missing_num(lst))