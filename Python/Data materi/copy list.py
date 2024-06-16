a = ["as","sd","hg"]
b = a 

#merubah data list
a[0] = "bu"
b[1] = "we"
print(f"{a}")
print(f"{b}")
#membuat copy a dengan copy()
n = a.copy()
n[0] = "hj"
print(f"{a}")
print(f"{b}")
print(f"{n}")

print("alamat dari a ",hex(id(a)))
print("alamat dari b ",hex(id(b)))
print("alamat dari n ",hex(id(n)))

