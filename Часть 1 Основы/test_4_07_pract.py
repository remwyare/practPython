def str_to_float():
    """
    :return - float из строки
    """
    try:        
        s = input("Введите чисто float: ")
        return float(s)
    except ValueError:
        print ("ошибка ввода")
        

print(str_to_float())
print(str_to_float())
print(str_to_float())
