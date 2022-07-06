class Shape:
    def __init__(self):
        print("Создаем фигуру")
        
    def what_am_i(self):
        print("Я - фигура")

class Square(Shape):
    def __init__(self, w):
        print("Создаем Квадрат w = {}".format(w))
        self.width = w
        
    def calculate_perimetr(self):
        return self.width * 4

    def change_size(self, delta):
        self.width += delta
        

class Rectangle(Shape):
    def __init__(self, w, l):
        print("Создаем прямоугольник w = {}, l = {}".format(w,l))
        self.width = w
        self.len = l

    def calculate_perimetr(self):
        return self.width * 2 + self.len * 2




rect = Rectangle(2,4) # конструктор родителя не вызывается?
square = Square(4)
square.change_size(-2)
print(rect.calculate_perimetr())
print(square.calculate_perimetr())

rect.what_am_i()
square.what_am_i()
