#1
import os
import csv
f_path = os.path.join(
              "C:\\",
              "Users",
              "remwyare",
              "Desktop",
              "test.txt")
print(f_path)
with open(f_path, "r") as f:
    print(f.read())

#2
with open("otvet.txt", "w") as f:
    s = input("kak dela?")
    f.write(s)

#3
l = [["Звездные войны", "Терминатор", "Искуственный интелект"],
     ["Дурак", "Матильда", "Левиафан"],
     ["Люди в черном", "Я - робот", "Эволюция"]]
with open("rezult.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for row in l:
        w.writerow(row)
    
