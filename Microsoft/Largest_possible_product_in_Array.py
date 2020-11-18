
#* Asked in Microsoft

#? You are given an array of integers. Return the largest product that can be made by
#? multiplying any 3 integers in the array.

#! Example:

#? [-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.


#* Implementing Quicksort

def partition(arr, low, high):
  i = (low-1)         # index of smaller element
  pivot = arr[high]     # pivot

  for j in range(low, high):

      # If current element is smaller than or
      # equal to pivot
      if arr[j] <= pivot:

          # increment index of smaller element
          i = i+1
          arr[i], arr[j] = arr[j], arr[i]

  arr[i+1], arr[high] = arr[high], arr[i+1]
  return (i+1)
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
 
 
def quickSort(arr, low, high):
  if len(arr) == 1:
      return arr
  if low < high:

      # pi is partitioning index, arr[p] is now
      # at right place
      pi = partition(arr, low, high)

      # Separately sort elements before
      # partition and after partition
      quickSort(arr, low, pi-1)
      quickSort(arr, pi+1, high)

#* Quicksorting first so that we can have sorted array in O[1] space complexity
#* and O[nlogn] time complexity... Then find max of mul(first,second,last) [2 biggest minus values will be at start]
#* and mul(last Three) [obvious]... thats our answer!!
def maximum_product_of_three(lst):
  if len(lst)<3: return -1 #! Not Possible case
  
  quickSort(lst,0,len(lst)-1)
  return max((lst[0]*lst[1]*lst[-1]),(lst[-1]*lst[-2]*lst[-3]))

print(maximum_product_of_three([-4, -4, 2, 8]))
# 128 => -4*-4*8
print(maximum_product_of_three([1,4,10,2,-1,45]))
# 1800 => 4*10*45
