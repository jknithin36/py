def max_number(a,b):
    if a > b:
        return a
    else:
        return b


print(max_number(1,2))


# using max function

def max_f(a,b):
    return max(a,b)

print(max_f(1,2))


# using sort method

def max_s(a,b):
    l = [a,b]
    l.sort()
    return l[-1]

print(max_s(1,2))

# using ternary operator


a = 10
b= 20 
print(a if a> b else b)


