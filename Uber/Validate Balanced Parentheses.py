# * This problem was recently asked by Uber

#Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#- Open brackets are closed by the same type of brackets.
#- Open brackets are closed in the correct order.
#- Note that an empty string is also considered valid.

#Input: "((()))"
#Output: True

#Input: "[()]{}"
#Output: True

#Input: "({[)]"
#Output: False

class Solution:
    def isValid(self, s):
        open_stack = list()
        
        for i in s:
            if i == '(' or i == '{' or i == '[':
                open_stack.append(i)
            elif i == ')':
                if len(open_stack)==0: return False
                elif open_stack.pop() != '(':
                    return False
            elif i == '}':
                if len(open_stack)==0: return False
                elif open_stack.pop() != '{':
                    return False
            elif i == ']':
                if len(open_stack)==0: return False
                elif open_stack.pop() != '[':
                    return False
        
        if len(open_stack)!=0: return False
        return True
    
# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
