l = []
li =[1,2,3,4,5]
s = {1,2,3,4,5}
print(type(s))

se ={}

print(type(se))

dic = {"name": "Nithin", "age": 23, "gender": "Male"}


while dict:
    print(dic["name"])
    break


print(dic.get("name", None))

for key in dic:
    print(key ,"->" , dic[key])



class Node:
    def __init__(self, value):
        self.value  = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    
    def traverse(self): 
        temp= self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next

    
    def unique_traverse(self):
        li = []
        temp = self.head 

        while temp is not None:
            li.append(temp.value)
            temp = temp.next
        
        se = list(set(li))

        for i in se:
            print(i)



ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(3)
ll.append(4)

ll.traverse()
print("----")
ll.unique_traverse()

    


            



