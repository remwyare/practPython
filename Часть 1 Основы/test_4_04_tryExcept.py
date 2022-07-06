try:
    a = input("введите число:")
    b = input("введите еще число:")
    a = int(a) #возможно исключение - ValueError
    b = int(b)
    print(a/b) #ZeroDivisionError - ошибка деления на 0
except(ZeroDivisionError, ValueError): # обьекты исключения
    print("ошибка ввода")
