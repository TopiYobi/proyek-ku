data = 10

count = 1
for i in range(data):
    print("*"*count)
    count += 1
print("akhir untuk FOR")

hitung = 1
while True:
    print("@"*hitung)
    hitung += 1

    if hitung > data:
        break
#data masih bisa di ubah

hitung = 1
F = int(data/2)
while True:
    if (hitung%2):
        print(" "*F,"^"*hitung)
        F -= 1
        hitung += 1
    else:
        hitung += 1
        continue
    if hitung > data:
        break



