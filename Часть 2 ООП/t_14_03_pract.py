class Square:
    list_s = []

    def __init__(self, l):
        self.len = l
        self.list_s.append(self)

    def __repr__(self):
        return str(self.len) + " на {}".format(self.len) * 3

def f(one, two):
    if one is two:
        return True
    else:
        return False

s1 = Square(5)
s2 = Square(3)
s3 = Square(5)
s4 = s3

print(s1)
print(f(s3, s4))
print(Square.list_s)
