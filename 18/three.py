class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:  # if none return falsee understand this logic examples throughly
            yield curNode
            curNode = curNode.next


class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    
    def __str__(self):
        values = [str(x) for x in self.LinkedList]
        return  " ".join(values)

    

    def isEmpty(self):
       return self.LinkedList.head is None
    
    def enQueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.LinkedList.head = new_node
            self.LinkedList.tail = new_node
        else:
            self.LinkedList.tail.next = new_node
            self.LinkedList.tail = new_node

    
    def deQueue(self):
        if self.isEmpty(self):
            return "Queue is Empty"
        else:
            temp_node = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
            return temp_node


    def peek(self):
        if self.isEmpty(self):
            return "Queue is Empty"
        else:
         return self.LinkedList.head.value
        

    

    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None
            
        