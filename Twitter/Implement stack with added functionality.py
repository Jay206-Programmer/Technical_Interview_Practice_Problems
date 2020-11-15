# asked by Twitter!

#Problem: Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of max() 
# which returns the maximum element in the stack (return None if the stack is empty). Each method should run in constant time.

class MaxStack:
    def __init__(self):
        self.stack = list()
    
    def push(self, val):
        self.stack.append(val)
        return self.stack
        
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    
    def findmax(self,st):
        return max(st)
    
    def max(self):
        return self.findmax(self.stack)
    
s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
