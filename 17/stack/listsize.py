class Stack:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list =[]

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return "\n".join(values)
    
    def isEmpty(self):
        return not self.list
    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else: 
            return False
    
    def push(self,value):
        if self.isFull():
            return "List is Full"
        else:
            self.list.append(value)
    

    def pop(self):
        if self.isEmpty():
            return "List is Empty"
        else:
            return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "List is Empty"
        else:
            return self.list[len(self.list)-1]
    

    def delete(self):
        return self.list.clear()


s = Stack(6)
print(s.isEmpty())
s.push(1)
s.push(2)
s.push(3)
s.push(5)
print(s)
s.pop()
print("--------")
print(s)
print("--------")
print(s.peek())

s.push(4)
s.push(5)
s.push(6)
print(s.push(7))
print(s)