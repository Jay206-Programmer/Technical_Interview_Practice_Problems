#* Asked in Facebook

#? Given a list, find the k-th largest element in the list.

#? Input: list = [3, 5, 2, 4, 6, 8], k = 3
#? Output: 5

from os import error


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    elif len(arr) == 2:
        if arr[-1]>=arr[0]: return arr
        else: return [arr[-1],arr[0]]
        
    middle = int(len(arr)/2)
    A = mergesort(arr[:middle+1]) 
    B = mergesort(arr[middle+1:])
    
    i,j = 0,0
    finalList = list() 
    while i<len(A) and j<len(B):
        if A[i] < B[j]:
            finalList.append(A[i])
            i+=1
        else:
            finalList.append(B[j])
            j+=1
    while i<len(A):
        finalList.append(A[i])
        i+=1
    while j<len(B):
        finalList.append(B[j])
        j+=1
    
    return finalList

#? Implemented Mergesort for O(nlogn) timeComplexity
def findKthLargest(nums, k = None):
    
    nums = mergesort(nums)
    n = len(nums)-k
    if n>=0:
        return nums[n]
    else:
        return "Given Key is Larger then Array Length!"
    
print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
# 5
print(findKthLargest([3, 5, 2, 4, 6, 8], 10)) #! cant have 10th largest element in 6 length array
# Error
print(findKthLargest([1,5,3,3,3,3,2,3,2,1,5,3], 6))
# 3

