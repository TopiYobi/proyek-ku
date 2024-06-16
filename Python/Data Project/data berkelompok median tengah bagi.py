i = int(input("masukan nilai p yang akan di tentukan = "))
pe = float(input("masukan jumlah data = " ))

r = (i/100) * pe
print(r)
tb = float(input("masukan kelas terbawah = "))
tb1 = tb - 0.5
print(tb1)
fk = float(input(f"masukan nilai fk sebelum {r} = "))
f = float(input("masukan frekuensi = "))
p = float(input("masukan panjang kelas = "))

hasil = r - fk
hasil1 = hasil/f
hasil3 = hasil1 * p
hasil4 = hasil3 + tb1

print(f"hasil dari median anda {hasil4}")
input("enter...........")



