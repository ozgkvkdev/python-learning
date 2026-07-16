# ==============================
# FOR DÖNGÜSÜ UYGULAMALARI
# ==============================

# Soru 1
# Sayılar listesindeki 3'ün katı olan sayıları bulun.

sayilar = [6, 7, 5, 15, 56, 45, 8, 9, 10]

print("Soru 1")
for sayi in sayilar:
    if sayi % 3 == 0:
        print(sayi)


# ------------------------------

# Soru 2
# Sayılar listesindeki sayıların toplamını bulun.

print("\nSoru 2")

toplam = 0

for sayi in sayilar:
    toplam += sayi

print("Toplam:", toplam)


# ------------------------------

# Soru 3
# Tek sayıların karesini yazdırın.

print("\nSoru 3")

for sayi in sayilar:
    if sayi % 2 == 1:
        print(sayi ** 2)


# ------------------------------

# Soru 4
# En fazla 5 karakterli şehirleri yazdırın.

print("\nSoru 4")

sehirler = ["istanbul", "adana", "mardin", "van"]

for sehir in sehirler:
    if len(sehir) <= 5:
        print(sehir)


# ------------------------------

# Ürün Listesi

urunler = [
    {"isim": "Samsung S6", "fiyat": "3000"},
    {"isim": "Samsung S7", "fiyat": "4000"},
    {"isim": "Samsung S8", "fiyat": "5000"},
    {"isim": "Samsung S9", "fiyat": "6000"},
    {"isim": "Samsung S10", "fiyat": "7000"},
]


# ------------------------------

# Soru 5
# Ürün fiyatlarının toplamını bulun.

print("\nSoru 5")

toplam = 0

for urun in urunler:
    toplam += int(urun["fiyat"])

print("Toplam fiyat:", toplam)


# ------------------------------

# Soru 6
# Fiyatı 5000 TL ve altında olan ürünleri yazdırın.

print("\nSoru 6")

for urun in urunler:
    if int(urun["fiyat"]) <= 5000:
        print(f"{urun['isim']} - {urun['fiyat']} TL")