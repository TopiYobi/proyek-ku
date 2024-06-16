data1 = [1,4,4,1,3,2,7,5,5,6,1,8,5,6,9,7,3,2]
print(f"data = \n{data1}")
 
## menghitung data (count)
jumlah_angka_4 = data1.count(4)
print(f"jumlah angka 4 = {jumlah_angka_4}")

## mengambil posisi data(index)
data2 = ["as","el","cl","ye"]
posisi_cl = data2.index("cl")
print(f"posisi cl = {posisi_cl}")

## mengurutkan data (sort())
# data int,float
print(f"data sebelum di sort = \n{data1}")
data1.sort()
print(f"data sesudah di sort = \n{data1}")
# data str
print(f"data sebelum di sort = \n{data2}")
data2.sort()
print(f"data sesudah di sort = \n{data2}")
## membalikan list (reverse()) ## sebelumnya harus di urut kan
# data int,float
print(f"data sebelum di balik = \n{data1}") 
data1.reverse()
print(f"data sesudah di dibalik = \n{data1}")
# data str
print(f"data sebelum di balik = \n{data2}") 
data2.reverse()
print(f"data sesudah di dibalik = \n{data2}")