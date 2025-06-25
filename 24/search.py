# Binary Search Tree

# left -> smaller than root

# right -> bigger than root





# using linkedlist and list 

# creation 
# insertion
#deletion
# Search

# Traverse

# delte



class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    

def insertNode(root, value):
    if root.data == None:
        root.data = value
    elif value <= root.data:
        if root.left is None:
            root.left = BSTNode(value)
        else:
            insertNode(root.left, value)
    else:
        if root.right is None:
            root.right = BSTNode(value)
        else:
            insertNode(root.right, value)
    return "The Node is Sucessfully Inserted"
    



def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)



def inOrderTraversal(rootNode):
    if not rootNode:
        return

    inOrderTraversal(rootNode.left)
    print(rootNode.data)
    inOrderTraversal(rootNode.right)


def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.data)



def levelOrderTraversal(rootNode):
    if not rootNode:
        return 
    
    else:
        pass



    


    
newBST = BSTNode(None)


insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)








# print(newBST.data)
print("----PREORDER---")

preOrderTraversal(newBST)

print("---INORDER----")

inOrderTraversal(newBST)
print("----POSTORDER---")

postOrderTraversal(newBST)

print("---LEVELORDER-----")

# creation --> Time and space --> O(1) and o(1)

