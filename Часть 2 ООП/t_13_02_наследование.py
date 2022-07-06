class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l
        
    def print_size(self):
        print("""фигура {} на {}
              """.format(self.width, self.len))

class Square(Shape): # Shape - родитель, Square - наследник(наследует все переменные и методы)
    def area(self):
        return self.width * self.len
    
    def print_size(self): # переопределение метода родительского класса
        print("""Квадрат {} на {}
              """.format(self.width, self.len))
        
        
my_shape = Shape(20, 25)
my_shape.print_size()

a_square = Square(20,20)
a_square.print_size()
print("площадь квадрата = {}".format(a_square.area()))


"""Композиция
class Dog():
    def __init__(self,
                 name,
                 breed,
                 owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Person():
    def __init__(self, name):
        self.name = name

mick = Person("Мик Джаггер")
stan = Dog("Стэнли",
           "Бульдог",
           mick)
print(stan.owner.name)
"""
