class Square:
    pass

class Rectangle():
    recs = [] # Переменная класса(глобальная для всех экземляров)

    def __init__(self, w, l):
        self.width = w 
        self.len = l  #width и len - переменные экземляра класса
        self.recs.append((w,l))

    def print_size(self):
        print("{} на {}".format(self.width, self.len))

print(Square) # Square - обьект "типа" Класс
sq = Square()
print(sq)

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs) #к переменным класса можно обращатся через обьект класса
