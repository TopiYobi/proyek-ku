# args (*)

#contoh penggunaan

def halo(*args):
    Nama = args[0]
    benua = args[1]
    print(f"Nama negara {Nama} Benua {benua}")

halo("Indonesia","Asia")

def jumlah(*jum):
    keluar = 0
    for i in jum:
        keluar += i
    return keluar

hasil = jumlah(1,2,3,4,5,6,8)
print(hasil)



