#Hampir sama materi dengan copylist

Datadict = {"As": "Amerika","Ind": "Indonesia","Jp":"Jepang","Jr": "Jerman"}
datacopy = Datadict.copy()

# Sehingga Alamat data akan berubah dan kita bisa mengubah salah satu data
print(f"Alamat Datadict = {hex(id(Datadict))}")
print(f"Alamat datacopy = {hex(id(datacopy))}")

# Mengubah data
Datadict["As"] = "united As"
print(Datadict)
print(datacopy)

# Pop data(Mengubah data berdasarkan key)
dataAs = Datadict.pop("As")
print("Data Yang diambil = ",dataAs)
print(Datadict)
# Popitem (Mengubah data terakhir)
dataJr = Datadict.popitem()
print("data terakhir = ",dataJr)
print(Datadict)
