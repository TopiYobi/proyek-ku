print(5*"="+"Kalkulatot"+10*"=")

n1 = int(input("masukan no pertama : "))
n2 = int(input("masukan no kedua : "))
op = input("""pilih oprasi 
A. +
B. X
C. /
D. -
pilihan = """)

if op=="a":
    hasil = n1 + n2
    print(f"hasil dari {n1} + {n2} = {hasil}")
    input("enter.....................")
elif op=="b":
    hasil = n1 * n2
    print(f"Hasil dari {n1} X {n2} = {hasil}")
    input("enter.....................")
elif op=="c":
    hasil = n1 / n2
    print(f"hasil dari {n1} / {n2} = {hasil}")
    input("enter.....................")
elif op=="d":
    hasil = n1 - n2
    print(f"hasil dari {n1} - {n2} = {hasil}")
    input("enter.....................")
else:
    print("maaf pilihan tidak tersedia..........")
    input("enter.....................")
