d1 = [1,2,3]
d2 = [4,5,6]

dd1 = [d1,d2,9]
dd1_c = dd1.copy()
print(f"data sekarang = {dd1}")
print(f"data sekarang = {dd1_c}")
# mengambil data dari nested list

dd2 = dd1[1][0]
print(f"Data yang terambil = {dd2}")

# Alamat data nested list
print(f"Alamat Data dd1 = {hex(id(dd1))}")
print(f"Alamat Data dd1_c = {hex(id(dd1_c))}")

# Alamat data list(member) Ke-1
print("Alamat data list(member) Ke-1")
print(f"Alamat Data dd1 = {hex(id(dd1[0]))}")
print(f"Alamat Data dd1_c = {hex(id(dd1_c[0]))}")

dd1[0][1] = 5
dd1[2] = 3
print(f"data sekarang = {dd1}")
print(f"data copy = {dd1_c}")

# Menggunakan Deep copy

from copy import deepcopy

dd1 = [d1,d2,9]
dd1_dc = deepcopy(dd1)
print(f"Alamat Data dd1 = {hex(id(dd1))}")
print(f"Alamat Data dd1_dc = {hex(id(dd1_dc))}")

print("Alamat data list(member) Ke-1")
print(f"Alamat Data dd1 = {hex(id(dd1[0]))}")
print(f"Alamat Data dd1_dc = {hex(id(dd1_dc[0]))}")

dd1[0][1] = 10
print(f"Data asli = {dd1}")
print(f"data copy = {dd1_c}")
print(f"data deepcopy = {dd1_dc}")

# kegunaan deepcopy yaitu untuk mengcopy lebih dalam untuk duplikasi list terutama nestedlist