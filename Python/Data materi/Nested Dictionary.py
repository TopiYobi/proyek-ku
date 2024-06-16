import datetime

Angota0 = {
    "Nama": "Jojo",
    "No Peserta": "123060",
    "Nilai": 90,
    "Menerima bantuan": False,
    "tanggal lahir": datetime.datetime(2002,3,4)
    }

Angota1 = {
    "Nama": "Adi",
    "No Peserta": "123045",
    "Nilai": 89,
    "Menerima bantuan": True,
    "tanggal lahir": datetime.datetime(2003,5,3)
}

Angota2 = {
    "Nama": "James",
    "No Peserta": "123078",
    "Nilai": 45,
    "Menerima bantuan": False,
    "tanggal lahir": datetime.datetime(1999,6,13)
}

DataAnggota = {
    "Pe_1": Angota0,
    "Pe_2": Angota1,
    "Pe_3": Angota2
}

print(f"{'NoKey':<6} | {'Nama':<17} | {'Tanggal lahir':<10} | {'No Peserta':<10} | {'Nilai':<8} | {'Menerima Bantuan':<2} ")
print("-"*84)

for semua in DataAnggota:
    KUNCI = semua
    NAMA = DataAnggota[KUNCI]["Nama"]
    NO_PE = DataAnggota[KUNCI]["No Peserta"]
    NILAI = DataAnggota[KUNCI]["Nilai"]
    MEBA = DataAnggota[KUNCI]["Menerima bantuan"] 
    LAHIR = DataAnggota[KUNCI]["tanggal lahir"].strftime("%x")
    print(f"{KUNCI:<6} | {NAMA:<17} | {LAHIR:<13} | {NO_PE:<10} | {NILAI:<8} | {MEBA:<2} ")

