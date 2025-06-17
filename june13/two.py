class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.head.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length+=1
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.head.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        self.length +=1
    
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index >self.length:
            return
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            
        self.length +=1
    
    def traverse(self):
        if self.head is None:
            print("List is Empty")
            return
        temp_node = self.head
        count =0
        while True:
            print(temp_node.value , end="->")
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            



#  Usage / Testing
cll = CircularLinkedList()

print("-- Append --")
cll.append(10)
cll.append(20)
cll.append(30)
cll.traverse()

print("-- Prepend --")
cll.prepend(5)
cll.traverse()

print("-- Insert at index 2 (should be 15 between 10 and 20) --")
cll.insert(2, 15)
cll.traverse()