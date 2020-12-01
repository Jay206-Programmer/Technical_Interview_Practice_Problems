
#* Asked in Amazon

#? Given a binary tree, find all the values stored at a given height

class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, height, count = 1, Arr = []):
  if height == count:
    return Arr.append(root.value)
  
  if root.left == None and root.right == None:
    print(Arr, count)
    
    return Arr
  
  elif root.left == None:
    return valuesAtHeight(root.right, height, count+1, Arr)
  
  elif root.right == None:
    return valuesAtHeight(root.left, height, count+1, Arr)
  
  else:
    Arr2 =  valuesAtHeight(root.left, height, count+1, Arr)
    Arr1 = valuesAtHeight(root.right, height, count+1, Arr)

    if Arr1 != None and Arr2 != None:
      return list(set([*Arr1,*Arr2]))
    elif Arr1 != None:
      return Arr1
    elif Arr2 != None:
      return Arr2
    else:
      return Arr

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(valuesAtHeight(a, 3))
# [4, 5, 7]


#     1
#    / \
#   2   3
#  / \   \
# 4   5   7
#        /
#       8

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
a.right.right.left = Node(8)
print(valuesAtHeight(a, 5))
# [8]