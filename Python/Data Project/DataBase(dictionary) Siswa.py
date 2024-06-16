import datetime
import os
import string
import random

Isidata = {
    "Nama": "Nama",
    "NISN": "000000",
    "Jurusan": "Jurusan",
    "Nilai Lulus": 0,
    "Tanggal Lahir": datetime.datetime(1111,1,11)
}

kumpulandata = {}
os.system("cls") # Membersihkan log sebelum
while True:
    print("="*5," Data Siswa Baru ","="*5)
    Informasisiswa = dict.fromkeys(Isidata.keys())
    Informasisiswa["Nama"] = input("Nama siswa : ")
    Informasisiswa["NISN"] = input("Masukan NISN siswa : ")
    Informasisiswa["Jurusan"] = input("Jurusan yang dipilih : ")
    Informasisiswa["Nilai Lulus"] = float(input("Nilai Terakhir SMP : "))
    TAHUN = int(input("Tahun Lahir (yyyy) : "))
    BULAN = int(input("Bulan lahir (1-12) : "))
    HARI = int(input("Tanggal lahir (1-31) : "))
    Informasisiswa["Tanggal Lahir"] = datetime.datetime(TAHUN,BULAN,HARI)
    
    KUNCI = ' '.join((random.choice(string.ascii_lowercase) for f in range(3)))
    kumpulandata.update({KUNCI:Informasisiswa})
    print(f"\n{'KODE':<4}  {'NAMA':>20}  {'NISN':>7}  {'JURUSAN':>10}  {'NILAI_LULUS':>3}  {'TANGGAL_LAHIR':>10}")
    print("-"*80)
    for Informasisiswa in kumpulandata:
        KUNCI = Informasisiswa
        NAMA = kumpulandata[KUNCI]["Nama"]
        NISN = kumpulandata[KUNCI]["NISN"]
        JURUSAN = kumpulandata[KUNCI]["Jurusan"]
        NILAI_LULUS = kumpulandata[KUNCI]["Nilai Lulus"]
        TANGGAL_LAHIR = kumpulandata[KUNCI]["Tanggal Lahir"].strftime("%x")
        print(f"{KUNCI:<4}  {NAMA:>20}  {NISN:>7}  {JURUSAN:>10}  {NILAI_LULUS:>3}  {TANGGAL_LAHIR:>10}")
    print("\ningin menambah data lagi (ya/tidak) y/t,,, ")
    h1 = input(">>>>> ")
    if h1 == 't':
        break
print(f"\n{'KODE':<4}  {'NAMA':>20}  {'NISN':>7}  {'JURUSAN':>10}  {'NILAI_LULUS':>3}  {'TANGGAL_LAHIR':>10}")
print("-"*80)
for Informasisiswa in kumpulandata:
    KUNCI = Informasisiswa
    NAMA = kumpulandata[KUNCI]["Nama"]
    NISN = kumpulandata[KUNCI]["NISN"]
    JURUSAN = kumpulandata[KUNCI]["Jurusan"]
    NILAI_LULUS = kumpulandata[KUNCI]["Nilai Lulus"]
    TANGGAL_LAHIR = kumpulandata[KUNCI]["Tanggal Lahir"].strftime("%x")
    print(f"{KUNCI:<4}  {NAMA:>20}  {NISN:>7}  {JURUSAN:>10}  {NILAI_LULUS:>3}  {TANGGAL_LAHIR:>10}")
print("endline")
    
