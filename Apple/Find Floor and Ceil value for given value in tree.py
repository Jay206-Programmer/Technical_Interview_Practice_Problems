# Asked in Apple
#Given an integer k and a binary search tree, find the floor (less than or equal to) of k, 
# and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

#Here is the definition of a node for the tree.

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None): #O(n) Time
    
    #Main Logic(checks & updates floor and ceil values)
    if root_node.value < k:
        if floor == None: floor = root_node.value
        
        elif k-root_node.value < k-floor:
            floor = root_node.value   
    elif root_node.value > k:
        if ceil == None: ceil = root_node.value
        
        elif root_node.value-k < ceil-k:
            ceil = root_node.value

    #Traverser(Traverses the tree)
    if root_node.left == None and root_node.right == None:
        pass

    elif root_node.left == None:
        (floor,ceil) = findCeilingFloor(root_node.right,k,floor,ceil)
    
    elif root_node.right == None:
        (floor,ceil) = findCeilingFloor(root_node.left,k,floor,ceil)
    
    else:
        (floor,ceil) = findCeilingFloor(root_node.left,k,floor,ceil)
        (floor,ceil) = findCeilingFloor(root_node.right,k,floor,ceil)
    
    return (floor,ceil)

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.left.left = Node(1)
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(5,findCeilingFloor(root, 5))
# (4, 6)
print(14,findCeilingFloor(root, 14))
# (12, None) Because max value of the tree has no ceil value
print(10,findCeilingFloor(root, 10))
# (8, 12)
print(2,findCeilingFloor(root, 2))
# (1, 4)
print(1,findCeilingFloor(root, 1))
# (None, 2)