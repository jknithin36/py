# list 

#left child cell[2x]
# right child cell [2x+1]
# o is emrty 



class BinaryTree:
    def __init__(self, size):
        self.list = size * [None]
        self.lastUsedIndex =0
        self.maxSize = size

    def isFull(self):
        return self.lastUsedIndex+1 == self.maxSize

    
    def insert(self,value):
        if self.isFull():
            return "Binary Tree is Full"
        self.list[self.lastUsedIndex+1] = value
        self.lastUsedIndex+=1
        return "The Value is Successfully Inserted"
    
    def search(value):
        pass



newBT = BinaryTree(8)
print(newBT)
print(newBT.isFull())

newBT.insert("Drinks")
newBT.insert("Hot")
print(newBT.insert("Cold"))





