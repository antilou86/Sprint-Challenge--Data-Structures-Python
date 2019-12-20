from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def __repr__(self):
        return(f"{self.capacity}, {self.current}, {self.storage}")

    def append(self, item):
        #if at capacity, add to the last item in the list
        if self.storage.length == self.capacity:
            if self.current != None:
                self.current.value = item
                self.current = self.current.next
            else:
                self.storage.head.value = item
                self.current = self.storage.head.next
        else: 
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TO-DO: Your code here
        current_node = self.storage.head
        while current_node:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next
        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        if self.current == self.capacity:
            self.current = 0
        self.storage[self.current]=item
        self.current+=1
        
    def get(self):
        tempList = []
        for i in self.storage:
            if i is not None:
                tempList.append(i)
        return tempList
                
