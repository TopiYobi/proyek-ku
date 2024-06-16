import os

os.system("cls")
a = int(input("Masukan Tahun = "))

if a/400 == 0:
    print("Ini Merupakan tahun kabisat")
elif a/4 ==0:
    print("Ini mungkin tahun kabisat")
elif a/100==0:
    print("ini jauh tahun kabisat")
else:
    print("ini bukan tahun kabisat")