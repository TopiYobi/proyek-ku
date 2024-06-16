a = str(input("Nama = "))
b = str(input("Kelas = "))
c = int(input("Nilai = "))

if c > 50:
    print("\n","="*9)
    print(f"Nama : {a}")
    print(f"Kelas : {b}")
    print("Keterangan : Lulus")
else:
    print("\n","="*9)
    print(f"Nama : {a}")
    print(f"Kelas : {b}")
    print("Keterangan : Tidak Lulus")
