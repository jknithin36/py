""""

Tree

Non - linear data structure

- hierarcial relation ship between its elements 


Why 

Quicker and easier access to the data 

used tto hierarical data such as HTML TREE, File System 

types - 
Binary Search tree
Avl Tree
Red Black Tree
Trie


# Tree Terminology


Root - top node without any parent

edge - a link between parents and children

leaf - a node which doesnot have any children

Siblings - children of same parent

Ancestor - parent, grandparent and great grand parent of a node

Depth of Node - a length of the path from root to node

height of nod - a lendth from node to deepest node

length of tree

depth of tree



"""


# creation
# TreeNode class for a general tree structure
import QueueLinkedList

class TreeNode:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children if children is not None else []

    def __str__(self, level=0):
        ret = " " * level * 2 + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, node):
        self.children.append(node)


# Creating a simple tree
tree = TreeNode("Drinks")

# Add children to root
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
tree.addChild(tea)
tree.addChild(coffee)

# Add children to "Tea"
tea.addChild(TreeNode("Black Tea"))
tea.addChild(TreeNode("Green Tea"))

# Add children to "Coffee"
coffee.addChild(TreeNode("Espresso"))
coffee.addChild(TreeNode("Latte"))

# Print the tree
print(tree)

# tree = TreeNode("Drinks", [
#     TreeNode("Tea", [
#         TreeNode("Black Tea"),
#         TreeNode("Green Tea")
#     ]),
#     TreeNode("Coffee", [
#         TreeNode("Espresso"),
#         TreeNode("Latte")
#     ])
# ])


# using linkedlist 

# creation , insertion , deletion, search , traverse , deletion

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")

newBT.left = leftChild
newBT.right = rightChild

def preOrder(root):
    if not root:
        return
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)


def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.left)
    print(rootNode.data)
    inOrder(rootNode.right)
print(newBT)


def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.left)
    postOrder(rootNode.right)
    print(rootNode.data)



def levelOrder(rootNode):
    if not rootNode:
        return 
    else:
        customQueue = QueueLinkedList.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.left)


preOrder(newBT)
print("-----")

inOrder(newBT)
print("-----")
postOrder(newBT)
