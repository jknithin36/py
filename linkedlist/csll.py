class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class circular_single_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length =0

    def __str__(self):
        result = ""
        temp_node = self.head
        # for i in range(self.length):
        #     result += str(temp_node.value)
        # return result
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head: # here for start alrealy we updted tempnode .next so if will be not head at starting
                break
            result +="->"
        return result



    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

        
        self.length+=1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail =new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node # because of previos head value we are cangingto new 

        self.length+=1

    def insert(self, index, value):
     new_node = Node(value)
     if index > self.length or index <0:
         raise Exception("Index out of exception")
     if index == 0:
        if self.length ==0:
            self.head = new_node
            self.tail - new_node
            self.tail.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
     elif index == self.length:
         self.tail.next = new_node
         new_node.next = self.head
         self.tail = new_node
     else:
        temp_node = self.head
        for _ in range(index - 1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
     self.length += 1

# learn nested if here and new raise and exception use case

    def traverse(self):
         temp_node = self.head
         while temp_node is not None:
             print(temp_node.value)
             temp_node = temp_node.next
             if temp_node == self.head:
                 break
       
       
    
    def search(self, target):
        temp_node =self.head
        while temp_node is not None:
            if (temp_node.value == target):
                return True
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return False
            
        





csll = circular_single_linked_list()
print("----Append Methods-----")

csll.append(10)
csll.append(20)
csll.prepend(1)
csll.insert(1,50)
csll.insert(0,12)

# print(csll.head.value)

print("--Traverse---")
print(csll)
csll.traverse()
print("---Trvaerse---")
print(csll.search(1))
print(csll.search(1111))