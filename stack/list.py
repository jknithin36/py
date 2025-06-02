class Stack:
    def __init__(self):
        self.list = []

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
        return "Success"
    
    def pop(self):
        self.list.pop()
        return "Sucesss"
    
    def peek(self):
        return self.list[(len(self.list) -1)]
    
    def delete(self):
        self.list=[]

list_stack = Stack()
        
print(list_stack)
print(list_stack.isEmpty())
list_stack.push(1)
list_stack.push(2)
list_stack.push(3)
list_stack.push(4)

print(list_stack)

list_stack.push(5)
list_stack.pop()
print(list_stack)
print("-----Peek----")
print(list_stack.peek())