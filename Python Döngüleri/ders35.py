# ==============================
# BREAK ve CONTINUE UYGULAMALARI
# ==============================

# Break Örneği
# Kullanıcı 0 girene kadar sayı al, 0 girince döngüyü bitir.

print("BREAK ÖRNEĞİ")

while True:
    sayi = int(input("Bir sayı gir (Çıkmak için 0): "))

    if sayi == 0:
        print("Program sonlandırıldı.")
        break

    print(f"Girilen sayı: {sayi}")


# ------------------------------

# Continue Örneği
# 1 ile 10 arasındaki tek sayıları yazdır.

print("\nCONTINUE ÖRNEĞİ")

for sayi in range(1, 11):
    if sayi % 2 == 0:
        continue

    print(sayi)