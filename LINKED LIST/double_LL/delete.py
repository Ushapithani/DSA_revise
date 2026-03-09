class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    def deleteHead(self, head):
        if head is None:          # empty list
            return None
        if head.next is None:     # single node
            return None
        head = head.next          # move head forward
        head.prev = None          # detach old head
        return head