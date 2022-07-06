class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Создано!")

    def rot(self, days, temp):
        self.mold = days * temp

orl = Orange(10, "Темный апельсин")
print(orl)
orl.weight = 100
print(orl.weight)
print(orl.color)

or2 = Orange(8, "Светлый апельсин")
or3 = Orange(14, "Желтый апельсин")

orange = Orange(6, "Апельсин")
print("orange.mold = {}".format(orange.mold))
orange.rot(10,33)
print("orange.mold = {}".format(orange.mold))
