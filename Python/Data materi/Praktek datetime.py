import datetime as t

print ("masukan tanggal lahir anda")
tanggal = int(input("tanggal : "))
bulan = int(input("bulan : "))
tahun = int(input("tahun : "))

td1 = t.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda {td1} di {td1:%A}")

sekarang = t.date.today()
umur1 = sekarang - td1
umur2 = umur1.days // 365
umur3 = (umur1.days % 360) // 30

print(f"umur anda yaitu : ")
print(f"""{umur2} tahun
{umur3} bulan
{umur1}
""")