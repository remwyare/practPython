x = 10
while x >= 0:
    print('{}'.format(x))
    x -= 1
print("S novim godom!")    

qs = ["kak tebya zovyt? ",
      "tvoy <3 cvet? ",
      "4to ti delaew? "]
n = 0
while True:
    print("vvedite X dlya vixoda")
    a = input(qs[n])
    if a == "X":
        break
    n = (n + 1) % 3

i = 0
while i < 5:
    if i == 2:
        i += 1
        continue
    print(i)
    i += 1

while input("Y or N?") != "N":
    for i in range(1,4):
        print(i)
