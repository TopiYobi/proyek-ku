def tambah(*args):
    hasil = 0
    for i in args:
        hasil += i
    return hasil

def kurang(*args):
    hasil = args[0] if args else 0

    for i in args[1:]:
        hasil -= i
    return hasil


