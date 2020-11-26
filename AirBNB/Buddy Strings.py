
#* Asked in AirBNB

#? Given two strings A and B of lowercase letters, return true if and 
#? only if we can swap two letters in A so that the result equals B.

#! Example 1:
#? Input: A = "ab", B = "ba"
#? Output: true

#! Example 2:
#? Input: A = "ab", B = "ab"
#? Output: false

#! Example 3:
#? Input: A = "aa", B = "aa"
#? Output: true

#! Example 4:
#? Input: A = "aaaaaaabc", B = "aaaaaaacb"
#? Output: true

#! Example 5:
#? Input: A = "", B = "aa"
#? Output: false

class Solution:
  def buddyStrings(self, A, B):
    if len(A) != len(B): return False
    
    i = 0
    count = 0
    charDict = {}
    while i < len(A):
      if A[i]!=B[i]:
        count+=1
        if count > 2: return False
      charDict[A[i]] = charDict.get(A[i],0) + 1
      i+=1
      
    if count == 2: return True
    elif count == 0: 
      for i in charDict.keys():
        if charDict[i] > 1: return True
        else: return False
    else: return False

print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
print(Solution().buddyStrings('aabc', 'aabc'))
# True
print(Solution().buddyStrings('abc', 'abc'))
# False