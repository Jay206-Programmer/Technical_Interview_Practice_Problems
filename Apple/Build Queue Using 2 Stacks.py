
#* Asked in Apple

#? Implement a queue class using two stacks. A queue is a data structure that supports the FIFO protocol
#? (First in = first out). Your class should support the enqueue and dequeue methods like a standard queue.

class Stack:
  def __init__(self):
    self.lst = list()
    self.top = None
    
  def push(self, val):
    self.lst.append(val)
    self.top = val
    
  def pop(self):
    X = None
    if len(self.lst) != 0:
      X = self.lst[-1]
      self.lst = self.lst[:-1]
      try:
        self.top = self.lst[-1]
      except:
        self.top = None
    return X
  
  def __len__(self):
    return len(self.lst)
    
class Queue:
  def __init__(self):
    self.stack1 = Stack()
    self.stack2 = Stack()
    
  def enqueue(self, val):
    self.stack1.push(val)
    
  def dequeue(self):
    while len(self.stack1) != 0:
      self.stack2.push(self.stack1.pop())
    X = self.stack2.pop()
    while len(self.stack2) != 0:
      self.stack1.push(self.stack2.pop())
    return X
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3
