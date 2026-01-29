class node :
    def __init__(self, x = 0 , next = None):
        self.data = x
        self.next = next
class linkedlist:

    def insert(self, head,x):
        new_node = node(x)
        if head is None:
            return new_node
        new_node = node(x)
        new_node.next= head
        head =new_node
        return head

    
        