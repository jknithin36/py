# list 

# built in data structure 

# we can store collection of items

# it was ordered so we can access using indexes

# [] -- values in list is called element and items


# [1,2,3,4] , ["a", "b", "c", "d"]

# mutli type --> ["a", 1, 1.3]

# nested lists are also poosible matrices and three dimansinal data

# practice
a = [1,2,3,4]
print(a)
b = [1,2 ,"a", 1.9]
print(b)

c = [1,2,3,[4,5,6], [4,[6,8]]]


# access and traversing 
print(c[4][1])

for i in a:
    print(i)
for j in range(len(b)):
    print(b[j])

a = len(c)
index =0




li = [10, 20, 30,40,50,60,70,80,90]

# option 

print(10 in li)

def linear_search(list, target):
    for i , value in enumerate(list):
        if value == target:
            return i
        
    return "NotFound"

print(linear_search(li, 90))





# operations

a = [1,2,3]
b = [4,5,6]
c = a+b

print(c)


print([1,3,4]* 4)

print(len([1,2,3,4,5]))

print(max(a))
print(min(a))
print(sum(a))