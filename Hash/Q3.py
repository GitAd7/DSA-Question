# How Many Numbers are Smaller than the Current Number-1365
def smallernumbthancurr(nums):
    ans = [0]*len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j and nums[i] > nums[j]:
                ans[i] += 1
    return ans

nums = [2,4,6,8,4,2]
res = smallernumbthancurr(nums)
print('The list of smaller element than current is:', res)