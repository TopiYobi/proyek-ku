# (list) merupakan kode untuk membuat beberapa data jadi satu
# contoh perintah "list[data str,data int,data bool]" bisa satu tipe
# maupun campuran dan juga bisa di tambahkan dengan oprasi aritmatika

dt = [1,2,3,4] # list sederhana dan bisa di campur atau diubah dengan data lain nya seperti str dan bool
print(dt)

# list alternatif
data_range = range(0,10,2) #-->> range(start,stop,step)
print(data_range)
data_L = list(data_range)
print(data_L)

data_range2 = range(0,10) #-->> range(start,stop,step)
print(data_range2)
data_L2 = list(data_range2)
print(data_L2)

# list dengan for loop(list comprehension)
list_for = [i for i in range(0,10)]
print(list_for) # tanpa assignment

list_for2 = [c+2 for c in range(0,10)]
print(list_for2) # dengan assignment

#list dengan for menggunakan if
list_if = [ d for d in range(0,10) if d != 5]
print(list_if) #melakukan seleksi dengan if statement

list_if2 = [ d**2 for d in range(0,10) if d != 5]
print(list_if2) #melakukan seleksi dengan if statement dengan assignment

#contoh kasus untuk memilih genap ganjil
G1 = [a for a in range(0,10) if a%2 == 0]
print(G1) # genap
G2 = [b for b in range(0,10) if b%2 !=0]
print(G2) #ganjil