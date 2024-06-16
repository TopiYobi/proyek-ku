import os

def sambutan():
    os.system("cls")
    print("="*10)
    print("Hayy siap memulai hari.......")

def namaplayer():
    os.system("cls")
    ino = input("Masukan nama yang kamu mau : ")
    return ino

def lok1(ino):
    os.system("cls")
    print("""
    |
    |
    |
    |
    |
    |_________________________\n""")
    print(f"{ino} {'terbangun dan melihat waktu telah menunjukan pukul 02.30':}\n")
    print("1. Bangun")
    print("2. Lihat hp sebentar")
    lok_1 = input(">>> ")
    if lok_1 == "1":
        print("kamu terbangun dan langsung merapikan kamar tidur")
    if lok_1 == "2":
        print("kamu membuka hp dan scroll media sosial sampai kamu")
        print("tidak sadar waktu menunjukan pukul 03:40") 

while True:

    sambutan()
    ma = input("(y/n).....>>>>> ")
    if ma == "n":
        break
    nam = namaplayer()
    lok1(nam)
    oh = input("")
    if oh == "e":
        break



