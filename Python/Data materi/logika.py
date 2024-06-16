#funsi not,or,and,xor(^)
# jadi logika adalah suatu perintah yang akan meghasil kan nilai boolean

print("========NOT")

a = False
b = not a

print("b NOT a =",b)

print("========OR")

a = False
b = True
c = a or b
print(a,"or",b,"=",c)

a = True
b = True
c = a or b
print(a,"or",b,"=",c)

a = False
b = False
c = a or b
print(a,"or",b,"=",c)

a = True
b = False
c = a or b
print(a,"or",b,"=",c)

print("========AND")

a = False
b = True
c = a and b
print(a,"and",b,"=",c)

a = True
b = True
c = a and b
print(a,"and",b,"=",c)

a = False
b = False
c = a and b
print(a,"and",b,"=",c)

a = True
b = False
c = a and b
print(a,"and",b,"=",c)

print("========XOR")

a = False
b = True
c = a ^ b
print(a,"xor",b,"=",c)

a = True
b = True
c = a ^ b
print(a,"xor",b,"=",c)

a = False
b = False
c = a ^ b
print(a,"xor",b,"=",c)

a = True
b = False
c = a ^ b
print(a,"xor",b,"=",c)








