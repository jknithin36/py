# length

print(len([1,2,3,4,5,6,7,8,9]))

# using loop

count =0
a = [1,2,3,4,5,6,7,8,9]
for i in a:
    count +=1

print(count)


# max in a list

a = [10,40,2,59, 567,34]

print(max(a))

# using loop

largest = a[0]

for i in a:
    if i > largest:
        largest = i

print(largest)

a.sort()
print(a)

# swap two items in a list

a = [10,20,30,40,50]

# a[0] , a[4] = a[4], a[0]
a[0] = a[4]
print(a)



# using temp varaible

a=[10,20,30,40,50]
temp = a[2]
a[2] = a[4]
a[4] = temp
print(a)

# checking if elements exists or not

if 30 in a :
    print("Elements Exists inlist")
else:
    print("not There")

# using a loop

key = 50
flag = False

for val in a:
    if val == key:
        flag = True
        break

if flag:
    print("Element Exists")
else:
    print("Not There")

print("--------")

f = any(x == 30 for x in a)
print(f)

if a.count(30)> 0:
    print("present in List")



# index of an item

a = ["cat", "dog", "tiger"]

print(a.index("dog"))

#index(element, start, end)

# remove Duplicates

a =[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
# a= list(set(a))
# print(a)

res = []

# for i in a:
#     if i not in res:
#         res.append(i)


# print(res)

[res.append(i) for i in a  if i not in res]

print(res)


# isng from keys\

k = list(dict.fromkeys(a))
print(k)




# reverse a list in python

a.reverse()
print(a)

a= list(set(a))
print(a)
# a.reverse()
# print(a)

# using a Slicing
rev = a[::-1]
print(rev)

# using Reversed but it give a iterator so to creatte a list we should put in list class

revs = reversed(a)
s = list(revs)

print(s)

# sum of a list

res = sum(a)
print(res)

#using loop

resp =0

for val in a:
    resp += val

print(resp)

lo = sum([i for i in a])
print(lo)


# unpacking 

https://www.geeksforgeeks.org/python/python-lists/