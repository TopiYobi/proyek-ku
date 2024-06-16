#pass = melewati 
#continun = melanjut keatas loop
#break = mengakhiri loop ketika sampai tujuan


masukan = int(input("masukan angka : "))
data = 0
while True:
    data += 1

    print(f"angka sekarang {data}")
    if data == masukan:
        print("dapat")
        break

print("cukup")