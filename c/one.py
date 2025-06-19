# Binary Tree --> At most 2 Childrens

# Each Node has Two Childrens

# left and right children

# create a Binary Node

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None





root = BinaryTreeNode("SmartPhone")
ios = BinaryTreeNode("IOS")
android = BinaryTreeNode("Android")
apple = BinaryTreeNode("Apple")
pixel = BinaryTreeNode("Google Pixel")
samsung = BinaryTreeNode("Samsung")


root.left = ios
root.right = android

ios.left = apple
android.left = pixel
android.right = samsung



# preorder --> root --> left --> right

def preOrder(root):
    if root:
        print(root.data, end =" ")
        preOrder(root.left)
        preOrder(root.right)




print("-- Hello ---")
preOrder(root)
# Insertion - top to bottom (left to right)



print('')

# inorder ---> left, root, right
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end =" ")
        inOrder(root.right)




def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')


from collections import deque


def levelorder(root):
    if not root:
        return 
    queue = deque([root])
    while queue:
        currnet = queue.popleft()
        print(currnet.data, end =" ")
        if currnet.left:
            queue.append(currnet.left)
        if currnet.right:
            queue.append(currnet.right)
        
levelorder(root)






# a queue is like a line of peple waiting at a corner

# The person who comes forst servedfirst -> this is claaed fifi menthod

# enQuue - add person at the end 

# deuue - Remove the first elemenet 


# deque - python builtin method - Double ended Queueu


# we can add/ remove fro boh ends

# but we use it like rwgular end

# at at theend aooend and remove from front - pop left 



deque = deque()

deque.append("A")
deque.append("B")
deque.append("c")

print("")
print(deque)


frist = deque.popleft()
print(frist)


# why Queue is used in binart tree

# when Inserting a nne level by level 

# we need checkeach node in order 

# start from node Then its left and right then move to next lwvwl 


# Queue to check which node to check nect 



# root is a starting a point 


def insertNode(root, value):
    new_node = BinaryTreeNode(value)
    if not root:
        return new_node
    
    q = deque([root])


    while q:
        current = q.popleft()

        if not current.left:
            current.left = new_node
            return root
        else:
            q.append(current.left)
        
        if not current.right:
            current.right = new_node
            return root
        else:
            q.append(current.right)



# understand not 


print(not True)


# falsy values in python 

# none, Flase, 0, "", [], {}, (), set()

print(not [])



# basic


print(not True)
print(not False)

# numbers

print(not 0)
print(not 1)


# strings

print(not "")
print(not " ") # true
print(not "hello")


# None

print(not None)

print(not [1,2])
print(not [])



node = None
if not node:
    print("Node is empty")



# loop


lst =[]

while not lst:
    print("list is still EMpty") # for firsttime list is empty but secod time list s not emprty
    
    lst.append(1)




class Node:
    def __init__(self, value):
        self.vale = value
        self.next = None


head = None

if not head:
    print("The list is Empty")
        



"""
# to insert a node we use level order --> go from top to bottom ad left to right 

"""





# pythonic synatx

# usally appear in if stteents and while loops


# based on thuthiness anf falsiness values

# in python we dont have to do this 

x = 1

if x == True:
    print("Hello")


# instead we have shortcuts 

if x: 
    print("Hello")

if ["hello"]:
    print("x")


if not []:
    print("Empty")


# if x 

# if not x

# while x -- Keep liiing x has somethng 

# while not x -- loop while x is empty 


# if x is None : check if x has  no value ( pointer / tree checking)

# if x == []

# if x!= []

# lf len(x) == 0:


# if len(x) > 0:


# if x == ""


# if x :

# if not nde:

# if node:



 

# 




