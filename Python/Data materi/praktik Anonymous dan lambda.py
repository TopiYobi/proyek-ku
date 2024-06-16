#Penggunaan lambda

nilai = lambda ank:ank**2

print(f"Nilai Kuadrat {nilai(3)}")

nilai2 = lambda ank3,pow : ank3**pow

print(f"Nilai Pengkat {nilai2(3,4)}")

# shorting 

ls = ["Amerika","Jepang","Indonesia","jerman","swiss"]

ls.sort(key=lambda nama:len(nama))
print(ls)

da1 = [1,5,8,3,6,2,4,3,9,2,3]

datN = list(filter(lambda c : c < 5,da1))
print(datN)

#data genap 
Dant = list(filter(lambda a:(a%2==0),da1))
print(Dant)

#data ganjil
Dant2 = list(filter(lambda v : (v%2!=0),da1))
print(Dant2)

#data kelipatan
Dant4 = list(filter(lambda b:(b%4==0),da1))
print(Dant4)


#Anonymous
def pan(n):
    return lambda an2:an2**n

#metode bebas
print(pan(2)(6))
#dengan assignment
hasil = pan(3)
print(hasil(5))
