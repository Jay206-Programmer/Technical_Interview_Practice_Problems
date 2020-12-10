
#* Asked in Uber

#? You are given a string of parenthesis. Return the minimum number of parenthesis that would need to be removed 
#? in order to make the string valid. "Valid" means that each open parenthesis has a matching closed parenthesis.

#! Example:

# "()())()"

#? The following input should return 1.

# ")"

def count_invalid_parenthesis(string):
  count = 0
  for i in string:
    if i == "(" or i == "[" or i == "{":
      count += 1
    elif i == ")" or i == "]" or i == "}":
      count -= 1
  
  return abs(count)

print(count_invalid_parenthesis("()())()"))
# 1