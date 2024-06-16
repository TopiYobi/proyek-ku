fk = float(input("Masukan FK "))
dataTB = float(input("Masukan jumlah data "))
dataTBh = dataTB - 0.5
d1 = float(input("d1 "))
d1h = fk - d1
d2 = float(input("d2 "))
d2h = fk - d2
p = float(input("P "))

h1 = d1h + d2h
h3 = d1h * p
h2 = h3/h1
h4 = dataTBh + h2

print(h4)




