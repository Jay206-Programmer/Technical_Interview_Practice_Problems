#* Asked in Google

#? There are n people lined up, and each have a height represented as an integer. 
#? A murder has happened right in front of them, and only people who are taller than everyone in front of them are able to see what has happened. How many witnesses are there?

#? Example:
#? Input: [3, 6, 3, 4, 1]  
#? Output: 3
#? Explanation: Only [6, 4, 1] were able to see in front of them.

class Stack:
    def __init__(self):
        self.top = None
        self.array = list()
    
    def push(self,val):
        self.array.append(val)
        self.top = val

    def pop(self):
        if len(self.array) == 0:
            return None
        else:
            element = self.array.pop()
            if len(self.array) == 0: self.top = None
            else:self.top = self.array[-1]
            return element
        
    def hasValue(self):
        if len(self.array) > 0:
            return True
        else:
            return False
        
    def __call__(self):
        return self.array

#* Stack Solution => O(n^2) time complexity => Best Case O(n)
def witnesses(heights):
    stack = Stack()
    for i in heights:
        if stack.top == None or i < stack.top:
            stack.push(i)
        else:
            while stack.hasValue() and stack.top <= i:
                stack.pop()
            stack.push(i)
    print(stack())
    return len(stack())

print(witnesses([3, 6, 3, 4, 1]))
# 3
print(witnesses([10,2,3,2,3,7,4,5,2,1]))
# 5 => [10,7,5,2,1]
print(witnesses([]))
# 0 => None
