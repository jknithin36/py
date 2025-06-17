class StarCookie:
    def __init__(self, color = "White", weight = 10):
        self.color = color
        self.weight = weight
        
StarCookie1 = StarCookie("Red", 15)
print(StarCookie1.color)
StarCookie2 = StarCookie()
print(StarCookie2.__dict__)

print(StarCookie.__dict__)



# Initialzer - used to define attributs 

# def __init__(self):

# self is object itself