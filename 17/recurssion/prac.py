# Dsa With Python

# Built In dataStructures

# list , Tuples, Dict, Sets

# User Defined DataSStructres

# LinkedList, Stacks ,Queues, Trees, Graphs

"""
List 

List is ordered , indexbased, supports differrnt datatypes , mutable

In we have references of values instead of values 
"""


"""
In Python list is built in dynamic sized array ( automatically grows and shrinks)
we can all types of items including another lists

may contain mix tyoe of items

itis possible lists stores references insted of actual items 

allows duplicates

Mutable --> modify, replace, or delete
ordered
Access elements using indexes starting from 0
"""

# create

a =[10,20,30,40,50, True, "hello"]
print(a)

# Accessing 

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[5])

# check types

print(type(a[5]))
print(type(a[4]))

# ways to create a list

# 1 . Using Square Brackets

a = [1,2,3,4,5]
b =["apple","banana","cheery"]
c = [1, "hello", [1,2,True], False, 34.8]
print(a,b,c)
print(c[2][0])
print(c[2][1])

# 2. using list constructur

cons = list("iterable")
print(cons)

cons1 = list((1,2,3,4,5))
print(cons1)


cons2 = list([1,2,3,5,6])

print(cons2)


# creating a list with repeated items

rep = [None] * 6
print(rep)

# for list we can acceess elemenents using postive and negative indexes

a =[10,20,30,40,50]
print(a[0])
print(a[-1])

# add elemets -  append(), extend(),insert()

a.append(100)
a.extend([200,300,400])
a.insert(len(a),1000)
print(a)

# update

a[0] =0
print(a)

# remove, pop, clear, clear

a.pop()
print(a)
a.pop(-2)
print(a)
a.remove(0)
print(a)


del a[0]
print(a)


# a.clear()
# print(a)


# iteration

for i in a:
    print(i)

for i in range(len(a)):
    print(a[i])

len = len(a)
count=0
while len >0:
    print(a[count])
    count+=1
    len -=1



# nested lists in python

matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1])

# practice

r1 = 0
r2 = 11

li = list(range(r1,r2))
print(li)

# range function creates an iterator

lil = [x for x in range(r1,r2)]
print(lil)


# ways to create. dict of lists

d ={}
d["1"] = [1,2]
d["2"] = [1,2.3]
print(d)


# using zip function 

# k = ["Fruits", "vegetbles"]
# v = [["Mango", "Banana"], ["Carrot", "Spinach"]]

# d = dict(zip(k,v))
# print(d)



# length
l=[1,2,3,4,6]
print(len(l))