# contoh 1

def Halo_dunia(nama):
    print(f"halo negara {nama}")

Halo_dunia("Amerika")

def Hitung(angka1,angka2):
    '''fungsi hitung'''
    hasil = angka1 + angka2
    print(f"Hasil dari {angka1} + {angka2} = {hasil}")

Hitung(13,5)

def Fungsi_list(List_saya):
    ''' fungsi list'''
    List_saya[2] = "Jepang"
    data_masukan = List_saya.copy()
    for List_saya in data_masukan:
        print(f"Negara sekarang => {List_saya}")

listnya = ["Amerika","inggris","Belanda","Indonesia"]
Fungsi_list(listnya)
print(listnya)