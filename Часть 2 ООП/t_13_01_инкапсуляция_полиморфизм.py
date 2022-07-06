class PublicPrivateExample:
    def __init__(self):
        self.public = "безопасно"
        self._unsafe = "опасно" # переменые и методы с _ подразумевают что клиент не должен к ним обращатся на прямую
        
    def public_method(self):
        #клиенты могут это использовать
        pass
        
    def _unsafe_method(self):
        #клиенты не должны это использовать
        pass
        self.public = "безопасно"
        self._unsafe = "опасно"

#пример полиморфизма(один интерфей для разных типов данных)
print("privet")
print(200)
print(1.2)

print(type("privet"))
print(type(200))
print(type(1.2))
    
    
"""
# Рисование фигур
# без полиморфизма
shapes = [tr1, sq1, cr1]
for a_shape in shapes:
    if type(a_shape) == "Triangle":
        a_shape.draw_triangle()
    if type(a_shape) == "Square":
        a_shape.draw_square()
    if type(a_shape) == "Circle":
         a_shape.draw_circle()

# Рисуем фигуры
# с помощью полиморфизма
shapes = [tr1,
          sw1,
          cr1]
for a_shape in shapes:
    a_shape.draw()
"""
