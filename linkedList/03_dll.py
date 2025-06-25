# create Node 


class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None



class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    
    def isEmpty(self):
        return self.head is None

    def append(self,value):
        # create a node 
        new_node = Node(value)
        # 1st Edge case 
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1


    
    def prepend(self, value):
        # create a node
        new_node = Node(value)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1
    
    def insert(self, index, value):
        if index <= 0:
            self.prepend(value)
            return
        temp = self.head
        for _ in range(index -1):
            temp = temp.next
            



                        



