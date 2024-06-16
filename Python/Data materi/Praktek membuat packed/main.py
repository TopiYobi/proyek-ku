#(contoh 1)from matematika import Kurang_tambah
#(contoh 2)from matematika.kurang_tambah import tambah
#(contoh 3)from matematika.kurang_tambah import tambah as ta

from matematika.Kurang_tambah import tambah as tam
from matematika.Kurang_tambah import kurang as kur
from matematika.Kali_Bagi import kali as kal
from matematika.Kali_Bagi import bagi as bag
hasil = tam(8,5)
print(hasil)
hasil1 = kur(9,7)
print(hasil1)
hasil2 = kal(3,4,5)
print(hasil2)
hasil3 = bag(15,3)
print(hasil3)


