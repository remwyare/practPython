dict_a = {"1" : "смех",
          "2" : "синий",
          "3" : "я",
          "4" : "смех",
          "5" : "кривой"}
del dict_a["5"]
n = input("введите число: ")
if n in dict_a:
    print(dict_a[n])
else:
    print("не найдено.")
          
