# (**) kwargs

#contoh 
def fucn(**kwargs):
    print(kwargs)

fucn( Nama = "Amerika",Umur = 34,benua = "Amerika")

#atau

def fcn(**kwargs):
    Nama = kwargs["Nama"]
    Tinggi = kwargs["Tinggi"]
    Umur = kwargs["Umur"]
    print(f" Nama : {Nama} Tinggi : {Tinggi} Umur : {Umur}")

fcn(Nama = "Joni",Tinggi = 156, Umur = 14)

#kasus

def hitung(*args,**kwargs):
    keluar = 0
    if kwargs["pilihan"] == "tambah":
        for e in args:
            keluar += e
    elif kwargs["pilihan"] == "kali":
        keluar = 1
        for e in args:
            keluar *= e
    return keluar

hasil = hitung(2,1,3,4,2,5,6,5,pilihan = "tambah")
print(f"Hasil penjumlahan {hasil}")
hasil = hitung(2,1,3,4,2,5,6,5,pilihan = "kali")
print(f"Hasil perkalian {hasil}")




