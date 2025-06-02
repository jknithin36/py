class Queue:
    def __init__(self):
        self.items =[]

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self,value):
        self.items.append(value)
        return "Success"
    
    def dequeue(self):
        if self.isEmpty():
            return "No Elements Found"
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "No Elements"
        else:
            return self.items[0]
    
    def delete(self):
        self.items =[0]

custom_queue = Queue()
custom_queue.enqueue(1)
custom_queue.enqueue(2)
custom_queue.enqueue(3)
custom_queue.enqueue(4)
print(custom_queue)
custom_queue.dequeue()
print(custom_queue)
print(custom_queue.peek())


