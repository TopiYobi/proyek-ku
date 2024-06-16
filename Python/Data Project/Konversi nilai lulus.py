while True:

    a = int(input("Masukan nilai = "))

    if a >= 90:
        print("Nilai A ")
    elif a >= 80 and a <= 89:
        print("Nilai B ")
    elif a >= 60 and a <= 79:
        print("Nilai C ")
    elif a >= 33 and a <= 59:
        print("Nilai D ")
    else:
        print("Nilai F ")
    