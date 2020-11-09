#* Asked in Apple

#? You are given two singly linked lists. The lists intersect at some node. 
#? Find, and return the node. Note: the lists are non-cyclical.

#? Example:

#? A = 1 -> 2 -> 3 -> 4
#? B = 6 -> 3 -> 4

#? This should return 3 (you may assume that any nodes with the same value are the same node).

def intersection(a, b):
    while b!= None:
        temp = a
        while temp!= None:
            if temp.val == b.val: return temp
            else:
                temp = temp.next
            
        b=b.next
    return None
    
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def prettyPrint(self):
        c = self
        while c:
            print(c.val)
            c = c.next

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
c.prettyPrint()
# 3 4