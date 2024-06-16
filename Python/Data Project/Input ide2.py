def judul():
    print("="*5," Input Pertanyaan dan Jawaban ","="*5)
    print("-"*15,"\n")

def nama():
    na = input("Masukan Nama mu : ")
    return na

lsp = []
lsj = []
while True:
    judul()
    n3 = nama()
    print(f"Haiii {n3} ")
    in2 = int(input(f"Masukan jumlah pertanyaan kamu {n3} = "))
    da = 0
    while da < in2: 
        da += 1
        in3 = input(f"Masukan pertanyaan kamu {n3} : ")
        lsp.append(in3)
    da1 = 0
    while da1 < in2:
        da1 += 1
        in4 = input(f"Masukan Jawaban Kamu {n3} :")
        lsj.append(in4)
    print(f"Pertanyaan kamu {n3}------")
    for o in lsp:
        print(o)
    print(f"jawaban kamu kamu {n3}------")
    for y in lsj:
        print(y)
    print("Apakah mau menambahkan lagi (n/y)")
    h = input(">>> ")
    if h == "n":
        break
print(f"Pertanyaan kamu {n3}------")
for o in lsp:
    print(o)
print(f"jawaban kamu kamu {n3}------")
for y in lsj:
    print(y)
print("Copy sebelum keluar program......")
input(">>>>>......")

