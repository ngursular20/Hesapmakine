sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))
try:
    bolum = sayi1/sayi2
    print("Bölüm:",bolum)
except ZeroDivisionError:
    print("Bir sayıyı sıfıra bölemezsiniz.")