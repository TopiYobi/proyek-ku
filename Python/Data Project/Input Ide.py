import os
memo = []
def judul():
    os.system("cls")
    print("="*5," Program Input/Penyimpan Soal ","="*5,"\n")

def nama():
    na = str(input("Masukan nama : "))
    return na

def masukanjumlah():
    akn = int(input("masukan jumlah soal = "))
    return akn

def masukansoal(akn):
    da = 0
    while da < akn:
        da += 1
        e = input("Masukan soal nya : ")
        memo.append(e)
    return e

def Jawanban(akn):
    da = 0
    while da < akn:
        da += 1
        y = input(f"Masukan jawaban {da} : ")
        memo.append(y)
    return y 

def menyimpan(e,y):
    print(e)
    print(y)

while True:
    judul()
    n3 = nama()
    print(f"\nhayyy {n3}")
    jum = masukanjumlah()
    qr = masukansoal(jum)
    yu = Jawanban(jum) 
    menyimpan(qr,yu)
    break

