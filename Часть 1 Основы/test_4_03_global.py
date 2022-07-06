x = 5  # переменные вне функции или класса - Глобальные
y = 10
def f():
    global x
    x = 1
    print(x)
    print(y)
f()
print(x)
