class Stack:
    def __init__(self):
        self.list =[]

    
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return "\n".join(values)

    

    def isEmpty(self):
        if self.list == []:
            return True
        else: 
            return False
        
    
    def push(self,value):
        self.list.append(value)
        return f"Succesfully instered ${value} in stack"
    
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            value = self.list[len(self.list) -1]
            self.list.pop()
            return value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.list[len(self.list) -1]
        
    
    def delete(self):
        self.list = None




one = Stack()

one.push(1)
one.push(2)
one.push(3)
one.push(4)
print(one)
print("--------")

one.push(4)
one.pop()
print("--------")
print(one)
print("--------")

print(one.peek())

    
