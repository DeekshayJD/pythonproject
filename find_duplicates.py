def find_duplicates(nums):
    result=[]
    for num in nums:
        index=abs(num)-1
        if nums[index]<0:
            result.append(index+1)
        else:
            nums[index]=-nums[index]
    return result

nums=[4,3,2,7,8,2,3,1]
print(find_duplicates(nums))