class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    def reverseDLL(self, head):
        if head is None or head.next is None:
            return head

        current = head
        temp = None

        while current:
            # Swap prev and next
            temp = current.prev
            current.prev = current.next
            current.next = temp
            # Move to next node (which is current.prev after swap)
            current = current.prev

        if temp:
            head = temp.prev
        return head