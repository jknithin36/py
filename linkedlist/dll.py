class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        # return f"{self.prev} <-- {self.value} --> {self.next}"
        return str(self.value)

# basically we can also got to prev element (back wards)

# node = Node(10)
# print(node)


class Dll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail =new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length+=1
    
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node is not None:
                result += "->"
        return result
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1
    
    def traverse(self):
        tempNode = self.head
        while tempNode is not None:
            print(tempNode.value)
            tempNode = tempNode.next
    
    def reverse_traverse(self):
        tempNone = self.tail
        # while tempNone is not None:
        #     print(tempNone.value)
        #     tempNone = tempNone.prev
        while tempNone:
            print(tempNone.value)
            tempNone = tempNone.prev
    # check why both will work here

    def search(self, target):
        tempNode = self.head
        while tempNode:
            if(tempNode.value == target):
                return True
            tempNode= tempNode.next
        
        return False
    
    def get(self, index):
        if index <0 or index >= self.length:
            return None
        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node= self.tail
            for _ in range(self.length -1 , index, -1):
                current_node = current_node.prev
        return current_node

# nice logic understand it how index and range works together
    

    def set(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

        
        





dll = Dll()
dll.append(10)
dll.append(20)
dll.prepend(2)

dll.prepend(1)
print(dll)
# dll.traverse()
dll.reverse_traverse()
print(dll.search(10))