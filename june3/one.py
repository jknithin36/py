# class Node:
#     def __init__(self,value,name):
#         self.value = value
#         self.name = name
#         self.next = None



# a = Node(10, "Nithin")

# print(a.name)
# print(a.value)
# print(a.__dict__) # self stores all in dict form


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length =0
    
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "-->"
            temp_node = temp_node.next
        
        return result
    

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head = new_node
        self.length +=1
    
    def insert(self):
        pass




ll = LinkedList()
ll.append(3)
ll.append(4)
ll.prepend(2)
ll.prepend(1)

print(ll)
