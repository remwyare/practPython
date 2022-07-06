import csv
with open("st.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["odin",
                "dva",
                "tri"])
    w.writerow(["cetiri",
                "p9t'",
                "west'"])
with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter = ",") #итерируемый обьект для доступа к строкам
    for row in r:
        print(",".join(row))
        print(row)
    
    
