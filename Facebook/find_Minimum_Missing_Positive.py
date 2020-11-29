
#* Asked in Facebook

#? You are given an array of integers. Return the smallest positive integer that is not present in the array. 
#? The array may contain duplicate entries.

#? For example, the input [3, 4, -1, 1] should return 2 because it is the smallest positive integer that 
#? doesn't exist in the array.

#! Your solution should run in linear time and use constant space.

#? Obvious solution, but solves in O(nlogn) time
def first_missing_positive(nums):
  nums.sort()
  minNum = 1
  for i in nums:
    if i == minNum: minNum+=1
    
    elif i > minNum: return minNum
  return minNum 

#? we have to solve in O(n) time

''' Utility function that puts all  
non-positive (0 and negative) numbers on left  
side of arr[] and return count of such numbers '''
def segregate(arr, size): 
  j = 0
  for i in range(size): 
      if (arr[i] <= 0): 
          arr[i], arr[j] = arr[j], arr[i] 
          j += 1 # increment count of non-positive integers  
  return j
  
''' Find the smallest positive missing number  
in an array that contains all positive integers '''
def findMissingPositive(arr, size): 
      
  # Mark arr[i] as visited by making arr[arr[i] - 1] negative.  
  # Note that 1 is subtracted because index start  
  # from 0 and positive numbers start from 1  
  for i in range(size): 
    if (abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0): 
      arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1] 
            
  # Return the first index value at which is positive  
  for i in range(size): 
    if (arr[i] > 0):           
      # 1 is added because indexes start from 0  
      return i + 1
  return size + 1

def first_Missing_Positive(nums):
  # First separate positive and negative numbers  
  shift = segregate(nums, len(nums)) 
      
  # Shift the array and call findMissingPositive for  
  # positive part  
  return findMissingPositive(nums[shift:], len(nums) - shift)  

#print(first_missing_positive([3, 4, -1, 1]))
# 2

print(first_Missing_Positive([3, 4, -1, 1]))