# Given a Singly Linked List's head, remove the nodes with the value equal to given value. Return the Linked List after deleting the nodes.

# Ex:-
# Input: [1,2,6,3,4,5,6], val=6
# Output: [1,2,3,4,5]

# Input: [], val=1
# Output: []

# Input: [7,7,7,7], val=7
# Output: []

class SLLNode :
    def __init__(self, val, nextNode=None):
        self.val = val
        self.next = nextNode

    def insert(self, new_val):
        new_node = SLLNode(new_val)
        current = self
        while current.next is not None:
            current = current.next
        current.next = new_node


list_1_head = SLLNode(1)
list_1_head.insert(2)
list_1_head.insert(6)
list_1_head.insert(3)
list_1_head.insert(4)
list_1_head.insert(5)
list_1_head.insert(6)

def removeGavenValueNodes(head: SLLNode, key):
    if head == None:
        return head
    
    head.next = removeGavenValueNodes(head.next, key)
    if head.val == key:
        return head.next
    return head

def printSLL(head: SLLNode):
    current = head
    while current != None:
        print(current.val)
        current = current.next

printSLL(list_1_head)
newHead = removeGavenValueNodes(list_1_head, 6)
printSLL(newHead)

