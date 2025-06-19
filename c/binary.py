# a Binary tree is a tree -like structure 

# each node have 0, 1 and 2 children 

# each node has left and right child


# the topmost noe is the root 


# just like a family Tree 


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, emd =" ")
        inOrder(root.right)



