class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length =0

    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    def print_all(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next




l = LinkedList()
l.append(10)
l.append(20)
l.print_all()
