class LinkedList:
    def searchKey(self, head, key):
        current = head
        while current:
            if current.val == key:
                return True
            current = current.next
        return False 