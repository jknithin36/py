class Queue:
    def __init__(self):
        self.list = []

    
    def isEmpty(self):
        return not self.list
    

    def enqueue(self,value):
        self.list.append(value)
        return "Succesfully added to Queue"
    

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            self.list.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is Emmpty"
        else:
            return self.list[0]
    

    def delete(self):
        self.list.clear()

    
    def __str__(self):
        values = [str(x) for x in self.list]
        return " ".join(values)




q = Queue()
print(q.isEmpty())

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.peek())


q.dequeue()

print(q)



# insert - enqueue
# delete - enqueue