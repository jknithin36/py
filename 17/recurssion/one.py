def factorial(num):
    assert num >=0 and int(num) == num, "The Number must be a postive integer"
    if num in [0,1]:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(4))
# print(factorial(-4))



# Fabnocci in Recurssion


def Fibonacci(n):
    if n in [0,1]:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

    

print(Fibonacci(6))



# measure Recurssive Algorithm

def findMAxNumRec(sampleArray, n):
    if n ==1:
        return sampleArray[0]
    return max(sampleArray[n-1], findMAxNumRec(sampleArray, n-1))