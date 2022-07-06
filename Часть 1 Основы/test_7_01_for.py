name = "nikola"
for i in name:
    print(i)

shows = ["vo vse tyzhkie",    
         "friends",
         "fargo"]
for s in shows:
    s = s.upper()
    print(s)

for i, s in enumerate(shows):
    print(shows[i].lower())

animes = ["ataka titanow",
         "ost",
         "gul"]
all_shows = []
for show in shows:
    all_shows.append(show.upper())
for show in animes:
    all_shows.append(show.upper())
print(all_shows)

for i in range(0,10): #range - последовательность целых чисел 0 - 9
    print(i)

    
