# ==============================
# WHILE DÖNGÜSÜ 
# ==============================

# Soru 1
# 0 ile 100 arasındaki çift sayıları ekrana yazdırın.

print("Soru 1")

x = 0

while x <= 100:
    if x % 2 == 0:
        print(x)
    x += 1


# ------------------------------

# Soru 2
# Kullanıcı boş isim girerse tekrar isim istemeye devam edin.

print("\nSoru 2")

name = ""

while not name.strip():
    name = input("İsminizi giriniz: ")

print(f"Merhaba, {name}!")