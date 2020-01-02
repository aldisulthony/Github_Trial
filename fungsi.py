def sambutan():
    print("Halo Apa Kabar")
    print("Selamat Malam")
    print("Selamat Beristirahat")

def penjumlahan(a,b):
    return a+b

def kalkulator(a, b, op):
    if op == "+"   :
        return a+b
    elif op == "-" :
        return a-b
    elif op == "*" :
        return a*b
    elif op == "/" :
        return a/b
    else:
        print("Operasi Tidak Dikenal")

def cek_palindrom(kata):
    return kata == kata[::-1]