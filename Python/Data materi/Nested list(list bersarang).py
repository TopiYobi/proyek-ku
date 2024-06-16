datap1 = ["adudu",34,"laki-laki"]
datap2 = ["jany",24,"perempuan"]
datap3 = ["bokc",15,"laki-laki"]

alldata = [datap1,datap2,datap3,"hanya gabungan",1,12,1]
print(alldata)

# contoh kasus/penggunaan nested list
alldata = [datap1,datap2,datap3,]
print(alldata)
for p in alldata:
    print(f"Nama    : {p[0]}")
    print(f"Umur    : {p[1]}")
    print(f"Kelamin : {p[2]}\n")

## dengan refren
copy_data = alldata.copy();
print(copy_data)
datap1[0] = "dasa"
print(copy_data)
print(alldata)
