#* Asked in Amazon

#? Given an array of n positive integers and a positive integer s, 
#? find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

#? Example:
#? Input: s = 7, nums = [2,3,1,2,4,3]
#? Output: 2
#? Explanation: the subarray [4,3] has the minimal length under the problem constraint.

class Solution:
    
    #? Simple Recursive Solution, Very slow but good for starting point
    def minSubArrayLen(self, nums, s):
        
        #? Base Case: Return 1 if any single value is greater than key, because in this case len of subarray will be 1
        if len(nums) == 1:
            if sum(nums) >= s: return 1
            else: return 0
        
        #? Recursive cases
        else:
            sm = sum(nums)
            #? If sum of current full array is greater than key than it is also a answer candidate, if not than only recursions are answer candidates
            if sm >= s:
                return self.nonzeroMinimum(len(nums),self.minSubArrayLen(nums[:-1],s),self.minSubArrayLen(nums[1:],s)) 
            else:
                return self.nonzeroMinimum(self.minSubArrayLen(nums[:-1],s),self.minSubArrayLen(nums[1:],s))
    
    #? returns nonzero Minimum of all given values, if no nonzero values then returns zero 
    def nonzeroMinimum(self,*args):
        mini = 0
        for i in args:
            if i != 0:
                if not mini:
                    mini = i
                else:
                    if i<mini:
                        mini = i
        return mini
    
#TODO: Implement Using Dynamic Programming

print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
#Ans: 2
#? Subarray [4,3] => 4+3 == 7 which is >= 7

print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 10))
#Ans: 4
#? Subarray [1,2,4,3] => 1+2+4+3 == 10 which is >= 10

print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 55))
#Ans: 0
#? Sum of any subarray can't be >= key

print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 4))
#Ans: 1
#? Subarray [4] => Element itself is >= to key

