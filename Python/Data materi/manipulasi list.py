
#index(urutan data) dari kiri kekanan(0,1,2.....) dari kanan kekiri(....-4,-3,-2,-1)
data1 = ["as","in","vb","cx"]

## mengambil data dari list
data0 = data1[0]
print(f"data 1 = {data0}")
data0 = data1[-1]
print(f"data akhir = {data0}")
## mengetahui panjang data
pdt = len(data1)
print(f"panjang data = {pdt}")
## menambah item pada list sesuai dengan posisi
print(f"data sebelum = {data1}")

data1.insert(0,"GH")
print(f"data sesudah = \n{data1}")
# menambah di akhir
data1.append("df")
print(f"data akhir = \n{data1}")
## menambah list dengan list
databa = ["yu","da","el"]
data1.extend(databa)
print(f"data yang digabung = \n{data1}")

## merubah data
print(f"data sebelum diubah = \n{data1}")
data1[3] = "nom"
print(f"data yang diubah = \n{data1}")

## menghapus/meremove data
data1.remove("yu")
print(f"data yang di remove = \n{data1}")
# meremove data akhir
data1.pop()
print(f"data yang diremove = \n{data1}")