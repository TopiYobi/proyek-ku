## loop range list

a1 = [1,2,4,5,2,67,12]

kup = len(a1)

for e in range(kup):
    print(f"Angka = {a1[e]}")

## while 
print("=======================")
a1 = [1,2,4,5,2,67,12]

kup = len(a1)
dat = 0
while dat < kup:
    print(f"Angka = {a1[dat]}")
    dat += 1

# enumerate

print("==========================")

dat1 = [1,2,3,"as","ot","jh"]

for in1,dat21 in enumerate(dat1):
    print(f"Index = {in1} Data = {dat21}")