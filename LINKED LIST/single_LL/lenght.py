class linkedlist:
    def lenght(self , head):
        count_lenght = 0 
        current= head
        while current:
            count_lenght +=1
            current = current.next 
        return count_lenght