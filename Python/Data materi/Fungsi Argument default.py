def Halo_dunia(nama = "Jepang"):
    print(f"halo {nama}")

Halo_dunia("Amerika")
Halo_dunia()

def pangkat(No1,No2 = 2):
    hasil = No1 ** No2
    print(hasil)

pangkat(2)

# atau

def pangkat2(N1 = 2,N2 = 2):
    hasil2 = N1 ** N2 
    return hasil2

print(f"Hasil dari pangkat {pangkat2(6)}") 
print(f"Hasil dari pangkat {pangkat2(5,7)}") 

# merubah/ mengakses argument dalam fungsi(def)

def input3(in1 = 1,in2 = 2,in3 = 3,in4 = 4):
    hast = in1 + in2 + in3 + in4
    return hast

print(input3(in3=5))
