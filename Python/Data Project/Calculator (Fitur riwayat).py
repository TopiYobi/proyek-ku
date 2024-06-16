import os
op = []

while True:
    os.system("cls")
    print ("\n","-"*6,"Kalkulator V2 ","-"*6)
    a1 = int(input("Masukan No Pertama = "))
    a2 = int(input("Masukan No Kedua   = "))
    print("="*5," Pilih Oprasi ","="*5)
    po2 = str(input(" + | - | * | / | % >>>.."))
    
    if po2 == "+":
        h1 = a1 + a2
        print(f"\nHasil Dari {a1} + {a2} = {h1}")
        op1 = [a1,a2,h1,po2]
        op.append(op1)
        print("\nKeluar dari Kalkulator(y/t)")
        h2 = str(input(">>>..."))
        if h2 == "y":
            break
    
    if po2 == "-":
        h1 = a1 - a2
        print(f"\nHasil Dari {a1} - {a2} = {h1}")
        op1 = [a1,a2,h1,po2]
        op.append(op1)
        print("\nKeluar dari Kalkulator(y/t)")
        h2 = str(input(">>>..."))
        if h2 == "y":
            break 

    if po2 == "*":
        h1 = a1 * a2
        print(f"\nHasil Dari {a1} * {a2} = {h1}")
        op1 = [a1,a2,h1,po2]
        op.append(op1)
        print("\nKeluar dari Kalkulator(y/t)")
        h2 = str(input(">>>..."))
        if h2 == "y":
            break 
      
    if po2 == "/":
        h1 = a1 / a2
        print(f"\nHasil Dari {a1} / {a2} = {h1}")
        op1 = [a1,a2,h1,po2]
        op.append(op1)
        print("\nKeluar dari Kalkulator(y/t)")
        h2 = str(input(">>>..."))
        if h2 == "y":
            break
    
    if po2 == "%":
        h1 = a1 % a2
        print(f"\nHasil Dari {a1} % {a2} = {h1}")
        op1 = [a1,a2,h1,po2]
        op.append(op1)
        print("\nKeluar dari Kalkulator(y/t)")
        h2 = str(input(">>>..."))
        if h2 == "y":
            break
    print("="*4," Riwayat Oprasi ","="*4)
    for inde,data in enumerate(op):
        print(f"Oprasi ke-{inde+1} Hasil dari {data[0]} {data[3]} {data[1]} = {data[2]}")
print("="*4," Riwayat Oprasi ","="*4)
for inde,data in enumerate(op):
     print(f"Oprasi ke-{inde+1} Hasil dari {data[0]} {data[3]} {data[1]} = {data[2]}")
input("Enter untuk keluar dari program>>>.......")