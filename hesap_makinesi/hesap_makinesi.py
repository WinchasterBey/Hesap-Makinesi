import time
import matplotlib.pyplot as plt
from random import choice

def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y != 0:
        return x / y
    else:
        return "Geçersiz işlem. Sıfıra bölme hatası!"

def kare(x):
    return x ** 2

def kup(x):
    return x ** 3

def print_header(efendim):
    print(r"""


                          WİNCHASTER


    """)
    print(f"\n Lancelot Hesap Makinesine - Hoş geldiniz")

def print_footer(name):
    print("\n*********************************************")
    print("Lancelot, Hesap Makinesi'ni kullandığınız için teşekkür ederiz. İyi günler! ")
    print("*********************************************")

def print_divider():
    print("\n================================================")

def main():
    name = "Lancelot"  # İsminizi burada "Lancelot" olarak değiştirebilirsiniz.
    emojis = ["", "", "", "", ""]  # İstediğiniz emojileri buraya ekleyebilirsiniz.

    print_header(name)
    

    while True:
        print_divider()
        print("\nİşlem Seçin:")
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Kare Hesapla")
        print("6. Küp Hesapla")
        print("7. Grafik Çiz")
        print("0. Çıkış")

        secim = input("Seçiminizi yapın (0-7): ")

        if secim == '0':
            print("\nHesap makinesi kapatılıyor...")
            print_footer(name)
            break

        if secim not in ['1', '2', '3', '4', '5', '6', '7']:
            print("\nGeçersiz giriş! Lütfen geçerli bir seçenek girin. ")
            continue

        if secim in ['1', '2', '3', '4']:
            sayi1 = float(input("\nBirinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))

            print("\nHesaplanıyor...")
            time.sleep(1)

            if secim == '1':
                sonuc = toplama(sayi1, sayi2)
                print(f"\n{sayi1} + {sayi2} = {sonuc:.2f} ")
            elif secim == '2':
                sonuc = cikarma(sayi1, sayi2)
                print(f"\n{sayi1} - {sayi2} = {sonuc:.2f} ")
            elif secim == '3':
                sonuc = carpma(sayi1, sayi2)
                print(f"\n{sayi1} * {sayi2} = {sonuc:.2f} ")
            elif secim == '4':
                sonuc = bolme(sayi1, sayi2)
                if isinstance(sonuc, str):
                    print(sonuc + " ")
                else:
                    print(f"\n{sayi1} / {sayi2} = {sonuc:.2f} ")

        elif secim == '5':
            sayi = float(input("\nBir sayı girin: "))
            sonuc = kare(sayi)
            print(f"\n{sayi}^2 = {sonuc:.2f} ")

        elif secim == '6':
            sayi = float(input("\nBir sayı girin: "))
            sonuc = kup(sayi)
            print(f"\n{sayi}^3 = {sonuc:.2f} ")

        elif secim == '7':
            x = [1, 2, 3, 4, 5]
            y = [kare(num) for num in x]

            plt.figure(figsize=(8, 6))
            plt.plot(x, y, marker='o', markersize=10, linestyle='-', linewidth=2, color='purple')
            plt.xlabel('X', fontsize=12)
            plt.ylabel('Y', fontsize=12)
            plt.title('Kare Grafiği', fontsize=14)
            plt.grid(True)
            plt.show()

main()
