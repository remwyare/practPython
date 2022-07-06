#3
films = ["xod9cie mertv",
         "krasavci",
         "klan soprano",
         "friends"]
for i, film in enumerate(films):
    print("films[{}] = {}".format(i,film))

#4
number = ["1","2","7"]
while True:
    s = input("put number or X (Exit)")
    if s == "X":
        break
    elif s in number:
        print("ygadal")
    else:
        print("neygadal")

#5    
x = [8,19,148,4]
y = [9,1,33,83]
z = []
for i in x:
    for j in y:
        z.append(i*j)
print(z)        
