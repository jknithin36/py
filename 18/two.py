class CircularQueue:
    def __init__(self, maxsize):   
       self.items = maxsize * [None]  # -----> o(1) , o(n)
       self.mazSize = maxsize
       self.start = -1
       self.top =-1
    


    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start ==0 and self.top +1 == self.mazSize:
            return True
        else:
            return False
        
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    

    
        



cq = CircularQueue(3)
print(cq.isFull())
    


        