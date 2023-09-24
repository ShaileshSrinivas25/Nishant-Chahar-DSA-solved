def sortedsquares(nums):
    for i in range(len(nums)):
            s = nums[i]
            nums[i] = s*s
    nums.sort()
    return nums
num =[-2,3,0,1,-9]
print(sortedsquares(num))
