#* Asked in AirBNB

#? You are given a singly linked list and an integer k. Return the linked list, 
#? removing the k-th last element from the list.

#! Try to do it in a single pass and using constant space.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)

def remove_kth_from_linked_list(head, k):
    i = 0
    itr = head
    flag = False
    while itr:
        if not flag and i > k:
            elementPointer = head
            elementNextPointer = head.next
            flag = True
        i+=1
        itr = itr.next
        if flag: 
            elementPointer = elementPointer.next
            elementNextPointer = elementNextPointer.next
            
    if k == i: return head.next
    elif k>i: return 'Value Error: Given index is larger than the linkedlist!'
    
    elementPointer.next = elementNextPointer.next
    return head 

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
head = remove_kth_from_linked_list(head, 3)
print(head)
# [1, 2, 4, 5]

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
head = remove_kth_from_linked_list(head, 5)
print(head)
# [ 2, 3, 4, 5]

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
head = remove_kth_from_linked_list(head, 1)
print(head)
# [1, 2, 3, 4]

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
head = remove_kth_from_linked_list(head, 10)
print(head)
# Error Message



