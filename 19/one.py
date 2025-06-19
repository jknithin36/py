# recurssion

def say_hello(n):
    if n ==0:
        return
    print(n)
    return say_hello(n-1)


say_hello(4)


# direct Recurssion - Function calls itself

# Indirect Recurssion 


# Tail Recurssion 


# Base Case and Recurssive Case

# Factorial of a Number

# facorial of 5 = 5 * 4 * 3 * 2* 1 = 120


def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)


print(factorial(5))


# sum of  Natural Numbers


def sume(num):
    if num == 1:
        return 1
    return num + sume(num-1)


print(sume(5))
    

# fabnocci Series

def fabonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fabonacci(num-1) + fabonacci(num-2)




