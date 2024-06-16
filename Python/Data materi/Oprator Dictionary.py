ls = ["as",2,"ucp"]

Data_dict = {
    "as": "Amerika",
    "Jp": "Jepang",
    "numb": 12346,
    "datls": ls
}

# Menghitung Panjang data 
Panjdat = len(Data_dict)
print(f"Panjang data dictionary = {Panjdat}")

# Mengecek Data 
kunci = "Jp"
kunci2 = "puc"
datacek = kunci in Data_dict
datacek2 = kunci2 in Data_dict
print(f"Apakah data {kunci} ada di Data_dict = {datacek} ")
print(f"Apakah data {kunci2} ada di Data_dict = {datacek2} ")

# mengakses data/read di dictionnary
print(Data_dict.get("as"))
print(Data_dict.get("GH"))# tanpa pesan
print(Data_dict.get("GH","data tidak di temukan")) # Dengan pesan

# Mengupdate data(Menambah dan mengubah)
Data_dict.update({"Jr": "Jerman"})
print(Data_dict)

# Menghapus data 
del Data_dict["Jp"]
print(Data_dict)
