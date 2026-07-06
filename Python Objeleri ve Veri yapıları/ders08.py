# ============================================
# PYTHON DERS 8
# Konu: String Formatlama (String Formatting)
# ============================================

# Değişkenlerimizi tanımlıyoruz.

ad = "Özgür"
soyad = "Kavak"

# --------------------------------------------
# 1. format() Metodu
# --------------------------------------------

# Süslü parantezler sırayla doldurulur.

print("Benim adım {} {}".format(ad, soyad))

print("---------------------------------")


# --------------------------------------------
# 2. İndis (Index) Kullanımı
# --------------------------------------------

# 0 = İlk değişken
# 1 = İkinci değişken

print("Benim adım {1} {0}".format(ad, soyad))

print("---------------------------------")


# --------------------------------------------
# 3. İsim Vererek Kullanma
# --------------------------------------------

print("Benim adım {ad} {soyad}".format(ad=ad, soyad=soyad))

print("---------------------------------")


# --------------------------------------------
# 4. Ondalıklı Sayıları Biçimlendirme
# --------------------------------------------

sonuc = 100 / 6

print("Sonuç :", sonuc)

# Virgülden sonra 4 basamak göster.

print("Sonuç : {s:1.4f}".format(s=sonuc))

print("---------------------------------")


# --------------------------------------------
# 5. f-String Kullanımı (Python 3.6+)
# --------------------------------------------

# Günümüzde en çok kullanılan yöntemdir.

print(f"Benim adım {ad} {soyad}")

print("---------------------------------")


# --------------------------------------------
# Mini Uygulama
# --------------------------------------------

urun = "Laptop"
fiyat = 35999.99

print(f"Ürün Adı : {urun}")
print(f"Ürün Fiyatı : {fiyat:.2f} TL")