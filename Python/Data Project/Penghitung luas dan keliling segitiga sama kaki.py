import os

def judul():
    os.system("cls")
    print("Selamat datang di Program penghitung luas dan keliling segitiga")
    print("="*19,"\n")

def masukanK():
    sisi = int(input("Masukan sisi segitiga = "))
    return sisi

def masukanL():
    Alas = float(input("Masukan Alas segitiga = "))
    Tinggi = float(input("Masukan Tinggi segitiga = "))
    return Alas,Tinggi

def keliling(sisi):
    return sisi+sisi+sisi

def luas(Alas,Tinggi):
    return 1/2 * Alas * Tinggi

def pesan(pe,va):
    print(f"Hasil perhitungan {pe} = {va}")

while True:
    judul()
    print("pilih oprasi :")
    print("a. Luas")
    print("b. Keliling")
    po = input(">>> ")    
    if po == "a":
        alas,tinggi = masukanL()
        l4 = luas(alas,tinggi)
        pesan("LUAS",l4)
        b = input("\nIngin keluar (y/n) >>> ")
        if b == "y":
            break
    if po == "b":
        st = masukanK()
        kle = keliling(st)
        pesan("KELILING",kle)
        c = input("\nIngin keluar (y/n) >>> ")
        if c == "y":
            break
print("program selesai")







    

