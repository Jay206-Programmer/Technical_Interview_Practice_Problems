# Asked in Twitter
# Reverse the Binary Tree

# You are given the root of a binary tree. Invert the binary tree in place. That is, 
# all left children should become right children, and all right children should become left children

# INPUT
#       a
#      / \
#     b   c
#    / \   \
#   d   e   f
# 
# OUTPUT
#       a
#      / \
#     c   b
#    /   / \
#   f   e   d 

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def preorder(self):
        print(self.value)
        if self.left: self.left.preorder()
        if self.right: self.right.preorder()

def invert(node):

    #Traverser(Traverses the tree)
    if node.left == None and node.right == None: return node

    elif node.left == None:
        node.right = invert(node.right)

    elif node.right == None:
        node.left = invert(node.left)

    else:
        node.left = invert(node.left)
        node.right = invert(node.right)

    #Swapper  
    temp = node.left
    node.left = node.right
    node.right = temp
    
    return node  

root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 

root.preorder()
# a b d e c f 
print("\n")
invert(root)
root.preorder()
# a c f b e d