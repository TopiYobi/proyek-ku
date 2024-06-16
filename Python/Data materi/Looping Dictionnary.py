Datdict = {
    "As": "Amerika",
    "Ind": "Indonesia",
    "Jp": "Jepang",
    "Jr": "Jerman",
}

for i in Datdict:
    print(i)

# Mengambil Item/ Itarables

## Hanya Mengambil Kunci
kunci = Datdict.keys()
print(kunci)
for k in kunci:
    print(k)

## Hanya mengambil Value(data)
nilai = Datdict.values()
print(nilai)
for l in nilai:
    print(l)

## Hanya mengambil item(Kunci dan data)
item = Datdict.items()
print(item)
for j in item:
    print(j)

## loop mengambil semua data (Data/key/item)

for kunci,data in Datdict.items():
    print(f"Key = {kunci} Value = {data}")