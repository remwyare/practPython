class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __repr__(self): #Метод наследуемый от класса Object для вывода на экран
        return str(self.n)

    def __add__(self, other): #Метод для a + b
        return abs(self.n + other.n)

class Person:
    pass
        

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x)
print(y)

print(x+y)

bob = Person()
same_bob = bob #переменные bob и same_bob ссылаются на один и тот же обьект
print(bob is same_bob) # is возвращает True если два обьекта являются одним и тем же обьектом


another_bob = Person()
print(bob is another_bob)

x = 10
print(x is None)
