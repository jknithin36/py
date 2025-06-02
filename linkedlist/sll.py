# Arrays are stored in line in memory 

# coming to Linked list 

# we want two blocks to store data and reference to next point 

# to access clearly we use head and tail and assign them starting and last elements 

# in memory in each node 

# there will be data and reference to next node 

# (1,ref2) --> (2, ref3) --> (3, None)

# for above frist elements we assign to head and 3rd element to tail

# first we are creating Node Class

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None # by default None

    
# new_node = Node(10)
# print(new_node)
# print(new_node.data)
# print(new_node.next)
# just like list access we can use . notation

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def __str__(self):
        tempNode = self.head
        result = ""

        
        while tempNode is not None:
            result += str(tempNode.value)
            if tempNode.next is not None:
                result += "->"
            tempNode = tempNode.next
        return result



    def append(self, value):
        # creating new node
        new_node = Node(value)
        # edge case
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # here if already there is anode then node consists self.next right that why self.next is available here
            self.tail = new_node
        self.length+=1

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    def insert(self , index , value):
        new_node = Node(value)

        if index < 0 or index > self.length:
            return False


        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        elif index ==0:
            new_node.next = self.head
            self.head = new_node
        
        else:
             
            temp_node = self.head
        
            for _ in range(index-1):
                temp_node= temp_node.next
        
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length+=1
        return True
    # understnad true and false logic and why mutlip if and else elif here (imean understand pattern ) 

    def traverse(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
            
        # here try with for loop too

# search value is present or not and return index
    def search(self, value):
        temp_node = self.head
        index = 0
        for i in range(self.length - 1):
            if(temp_node.value == value):
                return index
            else: 
                temp_node = temp_node.next
                index +=1
        return -1 
    
    # get value of index
    def get(self, index):
        #edge case
        if index <0 or index >= self.length:
            return None

        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        # return temp_node.value
        return temp_node # for set we method we are returning object instead of value

    
    # update value of given index with given value
    def set(self, index, value):
        temp = self.get(index)

        if temp is not None:
            temp.value = value
            return True
        return False
    # this method is using set method learn the sytanx

    def pop_first(self):
        if self.length ==0:
            return None
        popped_node = self.head

        if self.length == 1:
            self.head =None
            self.tail = None
        else:
           self.head = self.head.next
           popped_node.next = None
        self.length -=1
        return popped_node.value
# remember if used just if and below another logic if if is true and no return statement below statements also work 

    def pop(self):
        if self.length ==0:
            return None
        popped_node = self.tail
        if self.length ==1:
            self.head = self.tail = None # mutliple varibales same value
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                 temp_node = temp_node.next

        self.tail = temp_node
        temp_node.next = None
        
        self.length -=1

        return popped_node.value


    def remove(self, index):
        prev_node = self.get(index-1)
        popped_node = prev_node.next 
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -=1
        return popped_node
    
    # learn this logic it new


        

        
    def delete_all(self):
        self.head = None
        self.tail = None

    
    








        

        

    
    


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(40)
ll.prepend(0)
ll.insert(3, 30)
ll.insert(0, -1)
ll.insert(-3, 43)

# print(ll)
# print(ll.head)
# print(ll.head.value)
# print(ll.length)
# print(ll)
# print(ll.head.value)
# print(ll.tail.value)

print(ll)

ll.traverse()

print(ll.search(-1))
print(ll.search(78))

print(ll.get(3))

ll.set(0, -3)
ll.traverse()

print("-------Delete----- Methods")
print(ll.pop_first())
print(ll.pop())
print(ll.length)
print(ll.remove(10))
# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"Person : {self.name} - age {self.age}"


# new_person = Person("Nithin", "23")
# print(new_person)