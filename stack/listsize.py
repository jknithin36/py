class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list=[]

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
        
    def push(self,value):
        if self.isFull():
            return "Stack is Full"
        else:
            self.list.append(value)
            return "Success"
    
    def pop(self):
        if self.isEmpty():
            return "No elements to pop"
        else:
            popped_element = self.list.pop()
            return popped_element
    def peek(self):
        if self.isEmpty():
            return "No Elements Found"
        else:
            return self.list[len(self.list) -1]
        
    def delete(self):
        self.list =[]


list = Stack(4)
list.push(4)
list.push(3)
list.push(2)
list.push(1)
print(list)

list.push(5)
list.push(5)