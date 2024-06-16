#oprasi bitwise atau menghittumg biner
c = 9
v = 3


print("=======or(|)")
o = c | v

print("Nilai : ",c,",Biner : ",format(c,('08b')))
print("Nilai : ",v,",Biner : ",format(v,('08b')))
print("_____________________________________________(|)")
print("Nilai : ",o,",Biner : ",format(o,('08b')))

print("=======and(&)")
o = c & v

print("Nilai : ",c,",Biner : ",format(c,('08b')))
print("Nilai : ",v,",Biner : ",format(v,('08b')))
print("_____________________________________________(&)")
print("Nilai : ",o,",Biner : ",format(o,('08b')))

print("=======xor(^)")
o = c ^ v

print("Nilai : ",c,",Biner : ",format(c,('08b')))
print("Nilai : ",v,",Biner : ",format(v,('08b')))
print("_____________________________________________(^)")
print("Nilai : ",o,",Biner : ",format(o,('08b')))

print("=======not(~)")
o = ~v

print("Nilai : ",v,",Biner : ",format(v,('08b')))
print("_____________________________________________(~)")
print("Nilai : ",o,",Biner : ",format(o,('08b')))
b = 0b00000011
m = 0b11111111
print(m)
x = m ^ b
print("Nilai : ",x,"Biner : ",format(x,('08b')))

print("=======shift right(>>)")
o = v >> 2

print("Nilai : ",v,",Biner : ",format(v,('08b')))
print("_____________________________________________(>>)")
print("Nilai : ",o,",Biner : ",format(o,('08b')))

print("=======shift left(<<)")
o = v << 2

print("Nilai : ",v,",Biner : ",format(v,('08b')))
print("_____________________________________________(<<)")
print("Nilai : ",o,",Biner : ",format(o,('08b')))




