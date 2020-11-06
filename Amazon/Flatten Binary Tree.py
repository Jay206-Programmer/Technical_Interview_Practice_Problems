#* Asked in Amazon

#* Given a binary tree, flatten the binary tree using inorder traversal. 
#* Instead of creating a new list, reuse the nodes, where the list is represented by following each right child. 
#* As such the root should always be the first element in the list so you do not need to return anything in the implementation, 
#* just rearrange the nodes such that following the right child will give us the list.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"

def flatten_bst(root):
    #? Leaf Node
    if root.left == None and root.right == None:
        return root
    
    #? Only right childe the give right child to recursion
    elif root.left == None:
        root.right = flatten_bst(root.right)
        return root
    
    #? Only left child then swap children and recursion on right child
    elif root.right == None:
        root.right = root.left
        root.left = None
        root.right = flatten_bst(root.right)
        return root
        
    #? Have bot children then append right child to left child, then swap children and then recursion on right
    else:
        temp1 = root.left
        temp2 = root.right
        
        #? Finding right end of left child
        while temp1.right != None:
            temp1 = temp1.right
        
        temp1.right = temp2
        root.right = temp1
        root.left = None
        
        root.right = flatten_bst(root.right)
        return root
        
n5 = Node(5)
n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n5)
n1 = Node(1, n2, n3)

#      1
#    /   \
#   2     3
#  /     /
# 5     4

flatten_bst(n1)
print(n1)

# n1 should now look like
#   1
#    \
#     2
#      \
#       5
#        \
#         3
#          \
#           4
