#2
s_in = [];
s_in.append(input("Введите что то: "))
s_in.append(input("Введите что то: "))
rez = "Вчера я написал {}. Вчера я ходил в {}".format(s_in[0],s_in[1])
print(rez)

#3
print("\n3.")
rez = "мартин Лютер".capitalize()
print(rez)

#4
print("\n4.")
rez = "где это? когда это? кто это?".replace("? ","?&").split("&")
print(rez)

#5
print("\n5.")
l = ["rizhaya",
     "list",
     "pereprygnyla",
     "cerez",
     "zabor",
     "."]
rez = " ".join(l)
print(rez.replace(" .","."))

#8
print("\n8.")
rez = 'он скахал "Привет мир!"'
print(rez)

#9
print("\n9.")
print("tri"+"tri"+"tri")
print("tri" * 3)

#10
print("\n10.")
rez = "и незачем так орать! я первый раз..."
n = rez.index("!")
print(rez[:n])

