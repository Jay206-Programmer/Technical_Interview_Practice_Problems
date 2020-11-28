
#* Asked in Google

#? You are given a binary tree return deepest Node (Furthest node from root)

#! Example:

#?       a
#?     / \
#?    b  c
#?   /   
#?  d 

#! Ans: (d,3)

class Node(object):
  def __init__(self,val) -> None:
    self.val = val
    self.left = None
    self.right = None
    
  def __repr__(self) -> str:
    return self.val
  
def deepestNode(root,count = 1,max_count= 1,maxNode = None):
  if maxNode == None: maxNode = root
    
  if count > max_count:
    max_count = count
    maxNode = root
  
  if root.left == None and root.right == None:
    return (maxNode,max_count)
  
  elif root.left == None:
    maxNode,max_count = deepestNode(root.right, count+1, max_count, maxNode)
    return (maxNode,max_count)
  
  elif root.right == None:
    maxNode,max_count = deepestNode(root.left, count+1, max_count, maxNode)
    return (maxNode,max_count)
    
  else:
    maxNode,max_count = deepestNode(root.right, count+1, max_count, maxNode)
    maxNode,max_count = deepestNode(root.left, count+1, max_count, maxNode)
    return (maxNode,max_count)

root = Node('a')
root.left =Node('b')
root.left.left =Node('d')
root.right =Node('c')

print(deepestNode(root))
# (d,3)

root = Node('a')
root.left =Node('b')
root.left.left =Node('d')
root.left.left.right =Node('p')
root.left.left.right.right =Node('q')
root.left.right =Node('e')
root.right =Node('c')

print(deepestNode(root))
# (q,5)