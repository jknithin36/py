class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    
    def prepend(self,data):
        new_node= Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    
    def insert(self, index, data):
        if index <0 or index > self.length:
            return
        temp_node = self.head
        new_node = Node(data)
        if index ==0:
            self.prepend(data)
        elif index == self.length:
            self.append(data)
        else:
            for _ in range(index-1):
                temp_node= temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            
            



    
    def traverse(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.data)
            temp_node = temp_node.next

    def rev_traverse(self):
        my_list = []
        temp_node = self.head
        while temp_node is not None:
            my_list.insert(0, temp_node.data)
            temp_node = temp_node.next
        
        return my_list
    
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next 
            current.next = prev
            prev = current
            current = next_node

        
            
    




ll = LinkedList()
ll.append(20)
ll.append(40)
ll.prepend(10)
ll.insert(2,30)
ll.traverse()
print(ll.rev_traverse())


current = "a"
prev = "b"
next_of_current ="c"

next_node = next_of_current
