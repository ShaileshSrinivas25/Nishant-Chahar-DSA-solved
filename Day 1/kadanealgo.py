def maxsubarr(nums):
    """Find the maximum sum of a contiguous subarray in an array."""
    maxsum = nums[0] # Initialize with first element.
    cursum= nums[0]   # Current max value for current window.
    for num in nums[1:]:
        cursum = max(num,cursum+num)
        maxsum = max(maxsum,cursum)
    return maxsum
num = [-2,1,-3,4,-1,2,1,-5,4]
print(maxsubarr(num))


#  maxSum = float('-inf')
# currentSum = 0
        
#     for num in nums:
#         currentSum += num
            
#         if currentSum > maxSum:
#             maxSum = currentSum
            
#         if currentSum < 0:
#             currentSum = 0
        
#     return maxSum