
#* Asked in Twitter

#? You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.

#! Example:

#? [34, -50, 42, 14, -5, 86]

#? Given this input array, the output should be 137. 
#? The contiguous subarray with the largest sum is [42, 14, -5, 86].

#! Your solution should run in linear time.

#* Good Solution but does not run in a linear time
def max_subarray_sum(arr, hash = [], i = None, j = None):
  if not hash: hash = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
  
  if i!=None and j!= None:
    if hash[i][j] == -1:
      if len(arr) == 2:
        hash[i][j] = sum(arr)
        return hash[i][j]
      else:
        hash[i][j] = max(sum(arr),max_subarray_sum(arr[:-1],hash,i,j-1),max_subarray_sum(arr[1:],hash,i+1,j))
        return hash[i][j]
    else:
      return hash[i][j]
  else: #? First Iteration, i,j not defined
    i = 0 
    j = len(arr)-1
    if len(arr) == 2:
        hash[i][j] = sum(arr)
        return hash[i][j]
    else:
      hash[i][j] = max(sum(arr),max_subarray_sum(arr[:-1],hash,i,j-1),max_subarray_sum(arr[1:],hash,i+1,j))
      return hash[i][j]
  
#* Kadane's Algorithm O(n) time complexity
#! Limitation of this algorithm: Cant tell the biggest sum if the biggest sum is less than 0
def max_of_subarray(arr):
  maxTillNow = 0
  tempMax = 0
  
  for i in arr:
    tempMax+=i
    if tempMax < 0 : tempMax = 0
    if tempMax > maxTillNow: maxTillNow = tempMax
    
  return maxTillNow

#* Slower Solution
print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137

#* Faster Solution
print(max_of_subarray([34, -50, 42, 14, -5, 86]))
# 137


