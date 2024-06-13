def max_subarray(nums):
    total_sum=max_sum=nums[0]
    for i in nums[1:]:
        total_sum=max(i,total_sum+i)
        max_sum=max(max_sum,total_sum)
    return max_sum

nums=[-2,1,-3,4,-1,2,1,-5,4]
res=max_subarray(nums)
print(res)
