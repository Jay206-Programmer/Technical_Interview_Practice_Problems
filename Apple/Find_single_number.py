
#* Asked by Apple

#? Given an array of integers, arr, where all numbers occur twice except one number which occurs once, find the number.
#! Your solution should ideally be O(n) time and use constant extra space.

#! Example:

#? Input: arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]
#? Output: 7

#? Using Hash
#! This solution takes O(n) time but doesn't use constant space, This can be improved to take O(1) space
class Solution(object):
  def findSingle(self, arr):
    nums = {}
    for i in arr:
      nums[i] = nums.get(i,0) + 1
      
    for i,j in nums.items():
      if j == 1: return i
    
    return -1
  
nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3
