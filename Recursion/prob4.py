# Given the head of a singly linked list, reverse the linked list using recursion.

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
list_1_head.insert(3)
list_1_head.insert(4)
list_1_head.insert(5)

def reverseSinglyLinkedList(head):
    if head == None or head.next == None:
        return
    newHead = reverseSinglyLinkedList(head.next)
    head.next.next = head
    head.next = None

    return newHead

newHead = reverseSinglyLinkedList(list_1_head)
print(newHead)