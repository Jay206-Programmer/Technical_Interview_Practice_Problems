
#* Asked in Facebook

#? You are given the root of a binary search tree. Return true if it is a valid binary search tree,
#? and false otherwise. Recall that a binary search tree has the property that all values in the 
#? left subtree are less than or equal to the root, and all values in the right subtree are 
#? greater than or equal to the root.

class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

def is_bst(root, flag =  True):
  if root.left == None and root.right == None:
    return True
  
  elif root.left == None:
    flag = is_bst(root.right)
    if root.key > root.right.key: flag = False 
    return flag
    
  elif root.right == None:
    flag = is_bst(root.left)
    if root.key < root.left.key: flag = False 
    return flag
    
  else:
    flag = is_bst(root.right)
    flag = is_bst(root.left)
    if root.key > root.right.key or root.key < root.left.key: flag = False 
    
    return flag
    
a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)

print(is_bst(a))

#    5
#   / \
#  3   7
# / \ /
#1  4 6