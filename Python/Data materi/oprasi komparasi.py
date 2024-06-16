print("===Oprasi Komparasi===")
# setiap hasil koparasi merupakan Boolean
print("======== lebih besar dari(<)")
b = 3
c = 4

hasil = c < 7
print (c,'< 7 =',hasil)
hasil = b < 5
print (b,' < 5 = ',hasil)
hasil = c < b
print(c,'<',b,'=',hasil)

print("======== kurang dari dari(>)")
b = 3
c = 4

hasil = c > 7
print (c,'> 7 =',hasil)
hasil = b > 5
print (b,' > 5 = ',hasil)
hasil = c > b
print(c,'>',b,'=',hasil)

print("======== kurang dari sama dengan dari(>=)")
b = 3
c = 4

hasil = c >= 7
print (c,'>= 7 =',hasil)
hasil = b >= 5
print (b,' >= 5 = ',hasil)
hasil = c >= b
print(c,'>=',b,'=',hasil)

print("======== lebih dari sama dengan(<=)")
b = 3
c = 4

hasil = c <= 7
print (c,'<= 7 =',hasil)
hasil = b <= 5
print (b,' <= 5 = ',hasil)
hasil = c <= b
print(c,'<=',b,'=',hasil)

print("======== sama dengan(==)")
b = 3
c = 4

hasil = c == 7
print (c,'== 7 =',hasil)
hasil = b == 5
print (b,' == 5 = ',hasil)
hasil = c == b
print(c,'==',b,'=',hasil)

print("======== lebih besar dari(!=)")
b = 3
c = 4

hasil = c != 7
print (c,'!= 7 =',hasil)
hasil = b != 5
print (b,' != 5 = ',hasil)
hasil = c != b
print(c,'!=',b,'=',hasil)

# is dan is not
# merupakan komparasi sesama object atau variabel 
print("========= oprasi komparasi (is)") 
x = 4
y = 4

hasil = c is b
print(c,'is',b,'=',hasil)

print("========= oprasi komparasi (is not)") 
x = 4
y = 5

print("alamat object = ",hex(id(x)))
print("alamat object = ",hex(id(y)))

hasil = c is not b
print(c,'is not',b,'=',hasil)

# tips untuk melihat alamat object yang telah di tambahkan  
# pada terminal dengan masuk pada python lalu ketik "id(..)"
# dan untuk melihat nama pada object yaitu dengan mengetik "hex(id(..))"




