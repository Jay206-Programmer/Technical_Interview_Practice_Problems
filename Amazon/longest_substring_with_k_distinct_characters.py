
#* Asked in amazon

#? You are given a string s, and an integer k. Return the length of the longest substring in s 
#? that contains at most k distinct characters.

#? For instance, given the string:
#? aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.

def longest_substring_with_k_distinct_characters(s, k, maxLen = 0):
  
  chars = len(set(s))
  if chars == k:
    if len(s) > maxLen: maxLen = len(s)
  
  if maxLen != 0:
    return maxLen
  else:
    return max(longest_substring_with_k_distinct_characters(s[1:],k,maxLen),longest_substring_with_k_distinct_characters(s[:-1],k,maxLen))


print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)

print(longest_substring_with_k_distinct_characters('aabbbbbcddefff', 4))
# 10 (because 'aabbbbbcdd' has length 10 with 4 characters)
