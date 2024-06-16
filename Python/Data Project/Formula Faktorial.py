
def fa2(v):
    if v == 0 or v == 1:
        return 1
    else:
        return v * fa2( v-1)

ank1 = int(input("Masukan Angka Faktorial = "))
print(f"Hasil faktorial dari {ank1} = {fa2(ank1)}")