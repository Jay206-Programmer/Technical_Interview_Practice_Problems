
#* Asked by Twitter

#? Given an array, nums, of n integers, 
#? find all unique triplets (three numbers, a, b, & c) in nums such that a + b + c = 0.

#! Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be duplicates.

#! Example:

#? Input: nums = [0, -1, 2, -3, 1]
#? Output: [0, -1, 1], [2, -3, 1]

class Solution(object):
  def threeSum(self, nums):
    lst = []
    for i,val in enumerate(nums[:-2]):
      k = 0
      for val2 in nums[i+1:-1]:
        for val3 in nums[i+2+k:]:
          if val+val2+val3 == 0:
            lst.append([val,val2,val3])
        k+=1
    return lst

# Test Program
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]