#* Asked in Facebook

#? Given an array nums, write a function to move all 0's to the end of it while maintaining -
#? the relative order of the non-zero elements.

#? Example:
#? Input: [0,1,0,3,12]
#? Output: [1,3,12,0,0]
#? You must do this in-place without making a copy of the array.
#? Minimize the total number of operations.

class Solution:
    def moveZeros(self, nums):
        start_zero_index = -1
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                if start_zero_index == -1:
                    start_zero_index = i 
                
            else:
                nums[start_zero_index] = nums[i]
                nums[i] = 0
                start_zero_index+=1
            i+=1
            #print(nums)
        
        return nums

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]

