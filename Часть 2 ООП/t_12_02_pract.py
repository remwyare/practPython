import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return 2 * self.radius * math.pi

class Hexagon:
    def __init__(self, l):
        self.len_list = []
        for i in range(6):
            if i < len(l):
                self.len_list.append(l[i])
            else:
                self.len_list.append(1)
    def print(self):
        for len in self.len_list:
            print(len)
    def perim(self):
        p = 0
        for len in self.len_list:
            p += len
        return p    
    
#2
cir = Circle(5)
print(cir.area())


#4        
hex = Hexagon((3,4,5,2,7,9,10))
hex.print()
print("Периметр = {}".format(hex.perim()))
