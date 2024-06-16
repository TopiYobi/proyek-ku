# jadi aritmatika itu terdiri atas
# + penjumlahan
# - pengurangan
# * perkalian
# / pembagian
# ** perpangkatan
# // floor divisi
# % modulus

# contoh oprasi aritmatika sederhana

e = 10
c = 23
hasil = c + e # oprasi sedehana aritmatika

print(e,'+',c,'=',hasil)

# contoh oprasi aritmatika prioritas

a = 2
v = 3
s = 4
# jadi proses perhitungan nya yaitu
# 1, dalam kurung ()
# 2, perkalian
# 3,perpangkatan
hasil = s + v * a ** v / a // s - v % a
print (hasil)