class Node:
    """
    Creates the node class
    """
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class LinkedList:
    """
    Creates the linkedlist class
    """

    def __init__(self):
        self.head = None


    def traverse(self):
        """
        traverse through the entire linked list
        """
        out = []
        if not self.head:
            print("Linked list is empty")

        temp = self.head
        out.append(temp.item)

        while temp.next:
            temp = temp.next
            out.append(temp.item)

        return out


    def insert_start(self, item):
        """
        insert at the beginning
        """
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node


    def insert_at(self, item, index):
        """
        insert at the specified location or at the end if the linked list is not long enough
        """
        if index == 0 or (not self.head):            #if the location is at the beginning or the list is empty
            self.insert_start(item)
            return
        
        prev = self.head
        for i in range(1,index):
            if not prev.next:
                prev.next = Node(item)
            
            prev = prev.next
        
        temp = prev.next
        current = Node(item)
        prev.next = current
        current.next = temp


    def delete_head(self):

        if not self.head:
            return
        
        self.head = self.head.next
        
        self.head = self.head.next

    def delete_at(self, index):

        if not self.head:
            print("Linked list is empty")

        if index == 0:
            self.delete_head()

        prev = self.head
        current = prev.next

        for i in range(1,index):
            if current == None:
                print("Index out of range")
                return
            
            prev = current
            current = prev.next

        prev.next = current.next
        
        
        

        
        




linked_list = LinkedList()
linked_list.insert_at(10,3)
linked_list.insert_start(1)
linked_list.insert_last(3)
linked_list.insert_start(2)
linked_list.insert_last(4)
linked_list.insert_at(0,0)
linked_list.insert_at(50,3)
print(linked_list.traverse())