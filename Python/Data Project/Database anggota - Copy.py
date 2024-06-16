l1 = [ ]
while True:
    print("\n","="*4," Masukan Infomasi Anggota ","="*4)
    da1 = str(input("Masukan Nama Anggota \t: "))
    da2 = str(input("Masukan Alamat Anggota \t: "))
    da3 = int(input("Masukan Umur Anggota \t: "))

    allda = [da1,da2,da3]
    l1.append(allda)

    print("\n DataBase Angota ","="*10)
    for index,data in enumerate(l1):
        print(f"| No Anggota = {index+1}    Nama Anggota = {data[0]}    Alamat Anggota = {data[1]}    Umur Anggota = {data[2]}   |")

    print("\ningin menambah data lagi (ya/tidak) y/t,,, ")
    h1 = input(">>>>> ")
    if h1 == 't':
        break
print("end line")
input("......................")


        
