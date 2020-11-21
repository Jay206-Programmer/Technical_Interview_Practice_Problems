
#* Asked in Amazon

#? You are given an array stock market data, 
#? Try calculating the most money we can get!!

#! Example:

#? Data: [4,5,5,2,7,10,3]
#? Here we can get max 8rs of profit, if we buy at 2 and sell at 10

#* Naive approach: O(n^2) time Complexity
def func(arr):
  max = 0
  for i in range(len(arr)-1):
    temp_max = 0
    for j in range(i,len(arr)):
      if arr[j]-arr[i] > temp_max:
        temp_max = arr[j]-arr[i]
    if temp_max>max: max = temp_max
      
  return max

#* Faster Approach: O(n) time Complexity
def faster_func(arr):
  
  #? First create the array that contains max value of right sub array for each element
  rightMax = [-1]
  #? Staring from right 
  i = len(arr) - 2
  while i >=0:
    if arr[i] > rightMax[-1]:
      rightMax.append(arr[i])
    else:
      rightMax.append(rightMax[-1])
    
    i-=1
  #print(rightMax)
  
  #rightMax.reverse()
  #? We are not reversing to save the time
  #print(rightMax)
  max = 0
  i=0
  while i < len(arr)-1:
    if rightMax[len(arr)-i-1]-arr[i] > max:
      max = rightMax[i]-arr[i]
    i+=1
  return max

print(func([3,5,4,2,6,7,4,9,3]))
#7

print(faster_func([3,5,4,2,6,7,4,5,3]))
#5

print(faster_func([10,4,5,6,4,7,1,10,15,5]))
#14 => 15-1