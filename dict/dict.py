# dict

# create

#  1. Using Curly brackets

my_dict = {"name": "Nithin", "age": 23, "role":"Student"}

print(my_dict)

# 2. using dict() constructor


c_dict = dict(name="Nithin",  age=23, role= "Student")
print(c_dict)


# 3. using list of tuples or list of lists

t_dict = dict([("a",1), ("b", 2)])
print(t_dict)


# l_dict = dict[["a",1], ["b",1]]
# print(l_dict)

# 4. Using Comprension

co_list= {x: x*x for x in range(3)}
print(co_list)


# 5 using zip function

keys = ['a', 'b']

values =[1,2]

z_dict = dict(zip(keys,values))
print(z_dict)


# 6. from another dict 

# original = {'x': 10}
# copy_dict = dict(original)
# print(copyright)


# using from keys

f = {}.fromkeys([1,2,3])
print(f)

g = {}.fromkeys([1,2,3],0)
print(g)



# modify

h = {"a":1}

h["b"] = 2
print(h)
# add
h["a"] = 100
print(h)


j = {"x": 1}

# update method
j.update({"y": 2, "x": 100})
print(j)

# set default
 
sd = {"a":1}

sd.setdefault("a", 100) # does not change value becuses "a" is already exists only updates the if new kwy is found
sd.setdefault("b", 200)
print(sd)


#Change Keys or Values Manually

m = {'a': 1}

value  = m.pop("a")

m['b'] = 100
print(m)


# modiify all values in loop

l = {"x": 1, "y": 2}

for key in l:
    l[key] +=10
print(l)

# modify with dict operators

p = {"a": 1, "b": 2}

p = {k : v * 2 for k,v in p.items()}

print(p)


# nested array modification

student = {
    "name": "John",
    "scores": { "math": 20, "Social": 34},
    "age": 23
}

print(student)

print(student["scores"]["math"])


# deketing ways


d = {"a": 1, "b": 2}

del d["a"]

print(d)

# using pop


p = {"a": 1, "b": 1}

p.pop("b")
print(p)


# using pop item()

pi = {"a": 1, "b": 2}

print(pi.popitem()) # returns pop item in tuple


#using clear()

cl = {"a": 1, "b": 2}

cl.clear()
print(cl)


# Traverse 


t = {"name": "Nithin", "Age": 24, "role": "Student"}

for key in t: 
    print(key, t[key])


for value in t.values():
    print(value)


for key in t.keys():
    print(key)


for key, values in t.items():
    print(key , "--", values)


for i, (key, value) in enumerate(t.items(), 1):
    print(i, key, value)


print(sorted(t))

print(list(t))