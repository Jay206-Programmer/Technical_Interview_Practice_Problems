
#* Asked in Microsoft

#? You are given an array of intervals - that is, an array of tuples (start, end). 
#? The array may not be sorted, and could contain overlapping intervals. Return another array where the overlapping intervals are merged.

#! For example:
#! [(1, 3), (5, 8), (4, 10), (20, 25)]

#? This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).

#? Our approach will be to first sort the array and then simply loop through the array to check timings

def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
      
        # Sort each one and place into the result
        if left[left_cursor][0] <= right[right_cursor][0]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged

#* Using O(nlogn) time O[n] space
def merge_intervals(intervals):
  # Fill this in.
  intervals = merge_sort(intervals)
  
  i = 1
  finalArray = list()
  finalArray.append(intervals[0])
  while i<len(intervals):
    
    #? Current tuple compleately overlaps next tuple
    if finalArray[-1][1] >= intervals[i][1]:
      pass
    
    #? Current tuple partially overlaps next tuple
    elif finalArray[-1][1] >= intervals[i][0]:
      finalArray[-1] = (finalArray[-1][0],intervals[i][1])
      
    #? Current tuple does not overlap next tuple
    else:
      finalArray.append(intervals[i])
    
    i+=1
  
  return finalArray
  
print(merge_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]
print(merge_intervals([(1, 3), (5, 15), (4, 8), (10, 25)]))
# [(1, 3), (4, 25)]
print(merge_intervals([(5,10),(1,2),(3,4),(2,3)]))
# [(1, 4),(5,10)]

#! This program can be further improved by converting given array into linkedlist, it will give
#! O(nlogn) time and O(1) space complexity (Quicksort + Linkedlist)
