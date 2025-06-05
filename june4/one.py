# a way of solving problem by having a function calling itself

# russina doll

# properties

# performing same operation multiple times with diffferent inputs

# in every step we try smaller inputs to make problem smaller

# base condition is needed to avoid infinity loop

def openRussianDoll(doll):
    if doll == 1:
        print("All are opended")
    else:
        openRussianDoll(doll-1)
        print(doll)





openRussianDoll(5)



def powerofTwo(n):
    if n==0:
        return 1
    else: 
        power = powerofTwo(n-1)
        return power*2
    

# in stack memory base condition will work first because it is the last one to enter the stack

# space enfiecnt - o(n) 
# time effiecent  - no

# but easy to code




def powerofTwo1(n):
    i =0
    power = 1
    while i< n:
        power = power * 2
        i = i+1
    return power
    

print(powerofTwo(4))
print(powerofTwo1(4))

# how to write recurssion

# calls it self repeatedly until base condition met


# three step approach 
#1 Recusive case(flow
#2 Base condition
#3 edge cases 
# factorial - product of all postive integers 

def factorial(n):

    assert n>=0 and int(n) == n, "The number must be positive Integer only"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
# print(factorial(-1))





# import sys
# sys.setrecursionlimit(100000)
# how to incrase stack memory


def fibonacci(n):
    assert n>=0 and int(n) == n, "The number must be positive Integer only"

    if n in[0,1]:
        return n
    else:
      return fibonacci(n-1) + fibonacci(n-2)
    

print(fibonacci(6))


print("---sum of digits---")
# 1 . sum of digits 

# find the sum of digits of a positive integer using recusion

def sumofDigits(n):
    assert n >=0 and int(n), "The number must be Integer only"
    if n in [0,1,2,3,4,5,6,7,8,9]:
        return n
    else:
        return n%10 + sumofDigits(n//10)
    

print(sumofDigits(9))
print(sumofDigits(112))

print("---- power using recurssio ----")





print("------LOGIC__------")
records = [
    ("Alice", "Math", 85),
    ("Bob", "Math", 72),
    ("Alice", "English", 90),
    ("Bob", "English", 65),
    ("Alice", "Science", 88),
    ("Bob", "Science", 60)
]



my_dict = {}

for i in records:
    name = i[0]
    score = i[2]

    if name in my_dict:
        my_dict[name].append(score)
    else:
        my_dict[name] = [score]



for i in my_dict:
    



print(my_dict)
    