class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length+=1
        else:
            new_node= Node(value)
            self.tail.next = new_node
            self.tail = new_node
            self.length+=1

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "->"
            temp_node= temp_node.next
        
        return result
    

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail =new_node
            self.length +=1

        else:
            new_node.next = self.head
            self.head = new_node
            self.length +=1


    
    def insert(self, value, index):
        new_node = Node(value)

        if index < 0 or index > self.length:
          return False

        elif self.length ==0:
            self.head = new_node
            self.tail = new_node
        elif index ==0:
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
               temp_node = temp_node.next
        
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length+=1
        return True

    def traverse(self):
        current = self.head
        result = ""
        while current is not None:
            print(current.value)
            current = current.next
    
    def search(self, target):
        temp = self.head
        index =0
        while temp is not None: # why here just self.head insted of self.head.next
            if (temp.value == target):
                return index
            temp= temp.next
            index +=1

        return -1
        
    
    def get(self, index):

        if index  == -1:
            return self.tail # early returns
        if index <0 or index >= self.length:
            return None
        temp = self.head
        # while temp is not None:
        #     if (temp.value == target):
        #         return temp.value
        #     temp= temp.next

        for _ in range(index):
            temp = temp.next
        return temp
    

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):

        if self.length ==0:
         return None
        if self.length ==1:
            self.head = None
            self.tail = None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
        self.length-=1
        return popped_node
    
    # here learn why if instead of if elif and else - i know it will return early but what if we use elif there
    
    def pop(self):
        if self.length==0:
            return None
        if self.length ==1:
            self.head=None
            self.tail = None
        else:
            popped_node = self.tail
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length-=1
        return popped_node
    
    def remove(self, index):
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length-=1
        return popped_node
    

    
    # here leran everything why loopoing over self.tail and why we are using that techinque

    def delete_all(self):
        self.head=None
        self.tail = None
        self.length =0



    

            



    

        





    


l = LinkedList()
l.append(10)
l.append(20)
l.prepend(50)
l.insert(1, 2)
l.insert(30, 0)
l.traverse()

print(l.search(30))
print(l.search(100))

print(l.get(3))

l.pop_first()

l.remove(2)
print(l)
# p = LinkedList()
# # if new and there is nothing so it create a first node
# p.insert(20,0)
# print(p)

# differnce in while and foor