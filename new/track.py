tracking = {
    6 : "Wakeup",
    7 :"Gym",
    9: "Study",
    20: "Sleep"
}


from time import localtime

a = localtime()
hour = a.tm_hour
print(hour)

