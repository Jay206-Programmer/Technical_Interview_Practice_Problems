
#* Asked in Microsoft

#? A unival tree is a tree where all the nodes have the same value. Given a binary tree, 
#? return the number of unival subtrees in the tree.

#? For example, the following tree should return 5:

#!     0
#!   / \
#!  1   0
#!    / \
#!   1   0
#!  / \
#! 1   1

#? The 5 trees are:
#? - The three single '1' leaf nodes. (+3)
#? - The single '0' leaf node. (+1)
#? - The [1, 1, 1] tree at the bottom. (+1)

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def count(self, count = 0):
    if self.left == None and self.right == None:
      pass
    
    elif self.left == None:
      count+= self.right.count()
    
    elif self.right == None:
      count+= self.left.count()
    
    else:
      count+= self.left.count()
      count+= self.right.count()
    
    return count+1

def count_unival_subtrees(root):  
  if root.left == None and root.right == None:
    return 1
  
  elif root.left == None:
    n = count_unival_subtrees(root.right)
    
    if root.val == root.right.val and n == root.right.count():
      return n+1
    else:
      return n
    
  elif root.right == None:
    n = count_unival_subtrees(root.left)
    
    if root.val == root.left.val and n == root.left.count():
      return n+1
    else:
      return n
    
  else:
    n1 = count_unival_subtrees(root.left)
    n2 = count_unival_subtrees(root.right)
    
    if root.val == root.left.val and root.val == root.right.val and n1 == root.left.count() and n2 == root.right.count():
      return n1+n2+1
    
    else:
      return n1+n2
    
a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(count_unival_subtrees(a))
# 5

b = Node(0)
b.left = Node(1)
b.right = Node(0)
b.right.left = Node(0)
b.right.right = Node(0)
b.right.left.left = Node(1)
b.right.left.left.left = Node(1)
b.right.left.left.right = Node(1)
b.right.left.right = Node(1)
b.right.left.right.left = Node(1)
b.right.left.right.right = Node(1)

#!       0
#!     / \
#!    1   0
#!      / \
#!     0   0
#!    / \
#!   1   1
#!  /\  /\
#! 1 1 1 1

print(count_unival_subtrees(b))
# 8
