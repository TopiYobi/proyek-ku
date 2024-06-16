def jumlah(*args):
    b = 0
    for i in args:
        b += i
    return b

def kali(*args):
    b = 1
    for f in args:
        b *= f
    return b

def pangkat(n):
    return lambda ank:ank**n
