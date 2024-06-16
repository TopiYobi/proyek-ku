def jumlah(*pil):
    hasil = 0
    for i in pil:
        hasil += i
    return hasil

def kali(*pil):
    hasil = 1
    for i in pil:
        hasil *= i
    return hasil

def pangkat(n):
    return lambda ank:ank**n
